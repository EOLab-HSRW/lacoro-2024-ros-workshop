import xacro
from launch import LaunchDescription, LaunchDescriptionEntity
from launch.actions import IncludeLaunchDescription, OpaqueFunction, DeclareLaunchArgument
from launch.substitutions import EnvironmentVariable, PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def launch_args(context) -> list[LaunchDescriptionEntity]:

    declared_args = []

    declared_args.append(DeclareLaunchArgument(
        "namespace",
        default_value=EnvironmentVariable("ROBOT_NAMESPACE", default_value=""),
        description="Namespace for all topics and tfs",
    ))

    declared_args.append(DeclareLaunchArgument(
        "use_sim",
        default_value="true",
        description="Whether simulation is used",
    ))

    return declared_args

def launch_setup(context) -> list[LaunchDescriptionEntity]:

    robot_description_content = xacro.process_file(
        PathJoinSubstitution([
            FindPackageShare("rosbot_description"),
            "urdf",
            "rosbot.urdf.xacro"
        ]).perform(context),
        mappings={
                "use_sim": LaunchConfiguration("use_sim").perform(context),
                "use_gpu": "false",
                "mecanum": "false",
                "simulation_engine": "gazebo-classic",
                "namespace": LaunchConfiguration("namespace").perform(context)
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
            "-entity", "rosbot"]
    )

    return [
        robot_state_publisher,
        spawn_robot,
        launch_gazebo
    ]

def generate_launch_description() -> LaunchDescription:

    ld = LaunchDescription()

    ld.add_action(OpaqueFunction(function=launch_args))
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld
