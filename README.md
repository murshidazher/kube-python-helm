# [kube-python-helm](https://github.com/murshidazher/kube-python-helm)

An example repository for python microservice with k8s

- [kube-python-helm](#kube-python-helm)
  - [Developing](#developing)
    - [Create Virtual Environment](#create-virtual-environment)
  - [Up \& Running](#up--running)
  - [License](#license)

## Developing

### Create Virtual Environment

Isolate the dependencies using the python virtual environment.

```sh
python -m venv .venv
source .venv/bin/activate
```

Building the docker image

```sh
docker build -t webapp:1.0 .
docker run -d -p 5000:5000 --name web webapp:1.0 # to start
```

```
kubectl apply -f deployment.yml
kubectl apply -f service.yml


kubectl get pods
kubectl get service # http://localhost:30180/
```

To stop all the services in the directory

```sh
kubectl delete -f .
```

To get the service url

```sh
kubectl get pod && kubectl get service # k get pod,service
minikube service web-service
```

## Up & Running

```sh
cd src && python app.py
```

## License

[MIT] &copy; Murshid Azher.
