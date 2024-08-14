import sys
import urllib.request
import json

#Funcion para llamar a la API de GitHub
def conseguir_actividad(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read()
                eventos = json.loads(data)
                return eventos
            else:
                print(f"Error: code status {response.status}")
                return []
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} for {url}")
        return []
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason} for {url}")
        return []
    except Exception as e:
        print(f"Error desconocido: {e}")
        return []

#Funcion para mostrar por consola la actividad encontrada en GitHub
def mostrar_actividad(events):
    commit_counts = {}
    
    for event in events:
        event_type = event.get("type")
        repo_name = event.get("repo", {}).get("name")
        
        if event_type == "PushEvent":
            commits = len(event.get("payload", {}).get("commits", []))
            if repo_name in commit_counts:
                commit_counts[repo_name] += commits
            else:
                commit_counts[repo_name] = commits
        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action")
            print(f"{action.capitalize()} un problema en {repo_name}")
        elif event_type == "WatchEvent":
            print(f"Puntuado el repositorio {repo_name}")
        elif event_type == "CreateEvent":
            print(f"Creado el repositorio {repo_name}")

    for repo_name, count in commit_counts.items():
        print(f"Subido {count} commits a {repo_name}")


username = sys.argv[1]
events = conseguir_actividad(username)
if events:
    mostrar_actividad(events)
else:
    print("No se encontraron eventos en los datos recolectados.")