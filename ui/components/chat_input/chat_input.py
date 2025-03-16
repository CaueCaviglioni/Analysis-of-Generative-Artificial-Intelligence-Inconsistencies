import dash_bootstrap_components as dbc

def create_chat_input():
    return dbc.InputGroup(
        [
            dbc.Input(id="chat-input", placeholder="Ask a weird question...", autoComplete="off"),
            dbc.Button("Send", id="send-button", color="primary"),
        ]
    )