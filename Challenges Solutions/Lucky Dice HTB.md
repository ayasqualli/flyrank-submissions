## Solve Script

```python
import socket
import re

HOST = '154.57.164.75'
PORT = 32064

def solve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.settimeout(10)

    # We use a persistent buffer to read from the stream safely
    buffer = ""
    def read_until(marker):
        nonlocal buffer
        while marker not in buffer:
            try:
                chunk = s.recv(4096).decode('utf-8', errors='replace')
                if not chunk:
                    break
                buffer += chunk
            except socket.timeout:
                break
        
        if marker not in buffer:
            res = buffer
            buffer = ""
            return res
            
        idx = buffer.find(marker) + len(marker)
        res = buffer[:idx]
        buffer = buffer[idx:]
        return res

    # Intro
    intro = read_until('> ')
    print(intro, end='')
    s.sendall(b'1\n')

    for rnd in range(100):
        # STRATEGY CHANGE: Read until the question, NOT the prompt.
        # This gives us a massive head start before the 0.3s timer starts.
        output = read_until('Who wins this round?')
        print(output, end='')

        # Check if we triggered an error on the previous round
        if 'Mate... your are too slow' in output or 'scorring is off' in output:
            print("\n[!] Server error detected! We were too slow or wrong.")
            break

        lines = output.split('\n')
        players_ordered = []
        for line in lines:
            m = re.match(r'Player\s+(\d+):\s+([\d\s]+)', line.strip())
            if m:
                player_num = int(m.group(1))
                dice = list(map(int, m.group(2).strip().split()))
                players_ordered.append((player_num, sum(dice)))
                
        if not players_ordered:
            print('\n[!] Could not parse player scores!')
            print(repr(output))
            break
            
        max_score = max(score for _, score in players_ordered)
        winner = None
        # Your tie-breaker logic matches the server's stable sort perfectly
        for player_num, score in players_ordered:
            if score == max_score:
                winner = player_num
                
        print(f'\n  --> Round {rnd+1}: Winner = Player {winner} (score={max_score})')
        
        # PRE-FIRE: Send the answer IMMEDIATELY
        s.sendall(f'{winner}\n'.encode())

        # Now cleanly consume the rest of the options and the '> ' prompt 
        # so the buffer is clean for the next round.
        rest = read_until('> ')
        print(rest, end='')

    # Get the flag
    final = b''
    try:
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            final += chunk
    except socket.timeout:
        pass

    print('\n=== FINAL ===')
    print(final.decode('utf-8', errors='replace'))
    s.close()

if __name__ == '__main__':
    solve()
```