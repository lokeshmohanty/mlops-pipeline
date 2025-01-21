# Kubernetes

## Orchestration

## Minikube

Usefull for testing kubernetes features in your local machine

**Important Commands**:

-   Start: `minikube start`
-   Dashboard: `minikube dashboard`

## Important commands

-   Create deployment from image
```
	kubectl create deployment <name> --image=<image>
```

-   Expose a nodeport for a service to access it from outside
```
	kubectl expose deployment <name> --type=NodePort --port=<host-port>
```

-   Update the image
```
	kubectl set image deployments/<name> <name>=<new-image>
```

-   Rollback the image
```
	kubectl set image deployments/<name> <name>=<previous-image>
```

## References

-   [Kubernetes](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
-   [Minikube](https://minikube.sigs.k8s.io/docs/tutorials/kubernetes_101/)
