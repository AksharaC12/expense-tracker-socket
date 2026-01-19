import socket
import threading

from protocol import decode_request, encode_response
from auth import signup, login
from expenses import add_expense, get_expenses, delete_expense

HOST = "0.0.0.0"
PORT = 5000

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(4096)
            if not data:
                break

            request = decode_request(data)
            if not request:
                client_socket.send(
                    encode_response("error", "Invalid request format")
                )
                continue

            action = request.get("action")

            # ---------------- AUTH ----------------
            if action == "SIGNUP":
                success, msg = signup(
                    request["name"],
                    request["email"],
                    request["password"]
                )
                status = "success" if success else "error"
                client_socket.send(encode_response(status, msg))

            elif action == "LOGIN":
                success, result = login(
                    request["email"],
                    request["password"]
                )
                if success:
                    client_socket.send(
                        encode_response("success", "Login successful", result)
                    )
                else:
                    client_socket.send(
                        encode_response("error", result)
                    )

            # ---------------- EXPENSES ----------------
            elif action == "ADD_EXPENSE":
                add_expense(
                    request["user_id"],
                    request["category_id"],
                    request["amount"],
                    request.get("note"),
                    request["expense_date"]
                )
                client_socket.send(
                    encode_response("success", "Expense added")
                )

            elif action == "GET_EXPENSES":
                expenses = get_expenses(request["user_id"])
                client_socket.send(
                    encode_response("success", "Expenses fetched", expenses)
                )

            elif action == "DELETE_EXPENSE":
                delete_expense(
                    request["expense_id"],
                    request["user_id"]
                )
                client_socket.send(
                    encode_response("success", "Expense deleted")
                )

            else:
                client_socket.send(
                    encode_response("error", "Unknown action")
                )

        except Exception as e:
            client_socket.send(
                encode_response("error", "Server error")
            )
            break

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Socket server running on port {PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"Connected from {addr}")
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket,)
        )
        thread.start()

if __name__ == "__main__":
    start_server()
