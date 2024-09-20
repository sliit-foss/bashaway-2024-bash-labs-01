### check that pod is running with nginx server
```bash
kubectl exec -it nginx-deployment-6d6565499c-hjq4n -- curl -I http://localhost
```
