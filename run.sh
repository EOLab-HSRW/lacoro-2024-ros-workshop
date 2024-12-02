xhost +local:podman

podman run --rm -it --gpus all \
    --net=host \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    lacoro-2024 bash 

xhost -local:podman
