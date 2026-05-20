tickets = ["Chamado1","Chamado2","Chamado3"]
print("Tickets:",tickets)
print("Qual ticket deve ser removido?")
ticket = input()
if ticket in tickets:
    tickets.remove(ticket)
print("Tickets:",tickets)
