import re
file = open("5-1.in", "r")
lC = re.compile('aA|bB|cC|dD|eE|fF|gG|hH|iI|jJ|kK|lL|mM|nN|oO|pP|qQ|rR|sS|tT|uU|vV|wW|xX|yY|zZ')
Cl = re.compile('Aa|Bb|Cc|Dd|Ee|Ff|Gg|Hh|Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp|Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx|Yy|Zz')

for line in file:
    string = line.strip()

strs = list('abcdefghijklmnopqrstuvwxyz')

shortest = 50000
o_string = string
for repl in strs:
    remove = re.compile(repl + '|' + repl.upper())
    cont = True
    string = remove.sub('', string)
    while cont:
        prev_len = len(string)
        string = lC.sub('', string)
        string = Cl.sub('', string)

        if len(string) == prev_len:
            if len(string) < shortest:
                shortest = len(string)
            cont = False
    string = o_string

print(shortest)
