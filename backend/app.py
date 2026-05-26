from flask import Flask, jsonify
from flask_cors import CORS
from kubernetes import client, config
import os

app = Flask(__name__)
CORS(app)

def get_k8s_client():
    try:
        config.load_incluster_config()  # Inside K8s pod
    except:
        config.load_kube_config()  # Local fallback

@app.route('/api/nodes')
def get_nodes():
    get_k8s_client()
    v1 = client.CoreV1Api()
    nodes = v1.list_node()
    result = []
    for node in nodes.items:
        result.append({
            'name': node.metadata.name,
            'status': node.status.conditions[-1].type,
            'roles': node.metadata.labels
        })
    return jsonify(result)

@app.route('/api/pods')
def get_pods():
    get_k8s_client()
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces()
    result = []
    for pod in pods.items:
        result.append({
            'name': pod.metadata.name,
            'namespace': pod.metadata.namespace,
            'status': pod.status.phase,
            'node': pod.spec.node_name
        })
    return jsonify(result)

@app.route('/api/deployments')
def get_deployments():
    get_k8s_client()
    apps_v1 = client.AppsV1Api()
    deployments = apps_v1.list_deployment_for_all_namespaces()
    result = []
    for d in deployments.items:
        result.append({
            'name': d.metadata.name,
            'namespace': d.metadata.namespace,
            'replicas': d.spec.replicas,
            'ready': d.status.ready_replicas
        })
    return jsonify(result)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
