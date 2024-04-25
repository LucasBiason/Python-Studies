# Streamlit Aplicação Teste
Aplicação de teste do Streamlit Python


# Run 

  make run-app

# Access

  Local URL: http://localhost:8501


# Errors

In case of:

* OSError: [Errno 28] inotify watch limit reached

Run:
* echo fs.inotify.max_user_watches=524288 | sudo tee /etc/sysctl.d/40-max-user-watches.conf && sudo sysctl --system