import xacro
from launch import LaunchDescription, LaunchDescriptionEntity
from launch.actions import IncludeLaunchDescription, OpaqueFunction, DeclareLaunchArgument
from launch.substitutions import EnvironmentVariable, PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node, PushRosNamespace

def launch_args(context) -> list[LaunchDescriptionEntity]:

    declared_args = []

    declared_args.append(DeclareLaunchArgument(
        "robot_name",
        default_value=EnvironmentVariable("ROBOT_NAME", default_value="robot"),
        description="Namespace for all topics and tfs",
    ))

    declared_args.append(DeclareLaunchArgument(
        "use_sim",
        default_value="true",
        description="Whether simulation is used",
    ))

    return declared_args

def launch_setup(context) -> list[LaunchDescriptionEntity]:

    controllers_path_performed = PathJoinSubstitution([
        FindPackageShare("lsc_bringup"),
        "config",
        "controllers.yml"
    ]).perform(context)

    robot_description_content = xacro.process_file(
        PathJoinSubstitution([
            FindPackageShare("lsc_description"),
            "urdf",
            "rosbot.urdf.xacro"
        ]).perform(context),
        mappings={
            "robot_name": LaunchConfiguration("robot_name").perform(context),
            "controllers": controllers_path_performed,
        }
    ).toxml()

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="both",
        parameters=[
            {"robot_description": robot_description_content},
            # {"use_sim_time": LaunchConfiguration("use_sim_time")}, # TODO: Check if this is required
        ]
    )

    launch_gazebo = IncludeLaunchDescription(
        PathJoinSubstitution([
            FindPackageShare("gazebo_ros"),
            "launch",
            "gazebo.launch.py"
        ])
    )

    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        name="spawn_entity",
        arguments=[
            "-topic", "robot_description",
            "-x", "0",
            "-y", "0",
            "-z", "0.4",
            "-entity", LaunchConfiguration("robot_name")]
    )

    controller_manager_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "-p", controllers_path_performed,
            "joint_state_broadcaster",
        ],
    )

    return [
        PushRosNamespace(LaunchConfiguration("robot_name")), # this help to add robot_name to all entities
        robot_state_publisher,
        spawn_robot,
        launch_gazebo,
        controller_manager_spawner
    ]

def generate_launch_description() -> LaunchDescription:

    ld = LaunchDescription()

    ld.add_action(OpaqueFunction(function=launch_args))
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld
