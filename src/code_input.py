from dataclasses import dataclass
import textwrap

@dataclass(frozen=True)
class CodeLine:
    number: int
    text: str
    added: bool

@dataclass
class CodeFile:
    path: str
    lines: list[CodeLine]


def code_file_from_string("users.py", code) {
    return
}

def line_to_str(line: CodeLine) -> str:
    prefix = "+" if line.added else " "
    return f"{prefix} {line.number:>5} | {line.text}"

def render(file: CodeFile):
    for line in file.lines:
        print(line_to_str(line))




print(" --- File 1 ---")
code = textwrap.dedent("""\
    def get_user(conn, username):
        query = "SELECT * FROM users WHERE name = '" + username + "'"
        return conn.execute(query).fetchone()
""")
file = code_file_from_string("users.py", code)

print(" --- File 2 ---")
file = CodeFile("app/routes.py", [
    CodeLine(40, '@app.get("/orders")', added=False),
    CodeLine(41, "def list_orders():", added=False),
    CodeLine(42, '    customer = request.args.get("customer", "")', added=True),
    CodeLine(43, "    rows = conn.execute(\"SELECT * FROM orders WHERE customer = '\" + customer + \"'\")", added=True),
    CodeLine(44, "    return jsonify(rows)", added=False),
    CodeLine(19248, "    return jsonify(rows)", added=False),
])
render(file)