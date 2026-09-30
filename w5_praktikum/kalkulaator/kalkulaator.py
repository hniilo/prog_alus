import operator
import ast

BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

UNARY_OPS = {
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def arvuta(node):
    """Arvutab AST-puu sõlme väärtuse rekursiivselt.

    Mida teeb:
        - arv (ast.Constant) -> tagastab selle väärtuse;
        - kahe operandiga tehe (ast.BinOp, nt 2 + 3) -> arvutab vasaku ja
          parema poole ning rakendab neile BIN_OPS-ist leitud funktsiooni;
        - ühe operandiga tehe (ast.UnaryOp, nt -5) -> arvutab operandi ja
          rakendab UNARY_OPS-ist leitud funktsiooni.

    Miks nii:
        eval() käivitaks suvalist Pythoni koodi (nt faili kustutamine), mis on
        ohtlik. Siin lubame ainult arve ja teadaolevaid tehteid - kõik muu
        (muutujad, funktsioonikutsed, stringid jne) lükatakse tagasi.
        Rekursioon sobib, sest avaldis on puu: iga tehte operandid võivad
        omakorda olla tehted.

    Pane tähele: funktsiooni sees kutsutakse funktsiooni ennast välja (rekursioon)

    Raises:
        ValueError: kui sõlm pole lubatud tüüpi.
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in BIN_OPS:
        return BIN_OPS[type(node.op)](arvuta(node.left), arvuta(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPS:
        return UNARY_OPS[type(node.op)](arvuta(node.operand))
    raise ValueError("Lubamatu avaldis")


def kalkulaator(tekst: str):
    """Arvutab tekstina antud matemaatilise avaldise tulemuse.

    Mida teeb:
        1. asendab komad punktidega, et eesti stiilis kümnendmurrud (2,5)
           töötaksid;
        2. parsib teksti Pythoni AST-puuks (mode='eval' = üks avaldis);
        3. annab puu juure arvuta()-le, mis arvutab tulemuse.

    Miks nii:
        ast.parse teeb ära keerulise töö - tehete järjekorra (* enne +),
        sulud ja süntaksi kontrolli - ning me ei pea ise parserit kirjutama.
        Turvalisuse eest hoolitseb arvuta(), mis lubab ainult arvutustehteid.

    Raises:
        SyntaxError: kui tekst pole korrektne avaldis.
        ValueError: kui avaldises on lubamatuid elemente.
        ZeroDivisionError: nulliga jagamisel.
    """
    tekst = tekst.replace(',', '.')          # 2,5 -> 2.5
    puu = ast.parse(tekst, mode='eval')
    return arvuta(puu.body)


def main():
    """Käivitab kalkulaatori interaktiivse tsükli (REPL).

    Mida teeb:
        loeb kasutajalt korduvalt avaldisi, arvutab need kalkulaator()-iga ja
        prindib tulemuse. Tühja rea korral küsib uuesti, 'q'/'quit'/'exit'
        lõpetab programmi.

    Miks nii:
        kasutajaliides on arvutusloogikast eraldi, et kalkulaator()-it saaks
        testida ja teistes programmides kasutada ilma input()-ita. Vead
        püütakse siin kinni ja näidatakse arusaadava teatena, et programm
        ühe vigase sisendi peale kokku ei jookseks.
    """
    print("Kalkulaator. Sisesta avaldis (nt 2 + 3 * (4 - 1)) või 'q' lõpetamiseks.")
    while True:
        sisend = input("> ").strip()
        if sisend.lower() in ('q', 'quit', 'exit'):
            break
        if not sisend:
            continue
        try:
            print(kalkulaator(sisend))
        except ZeroDivisionError:
            print("Viga: nulliga ei saa jagada")
        except (SyntaxError, ValueError):
            print("Viga: vigane avaldis")
        except OverflowError:
            print("Viga: tulemus on liiga suur")


if __name__ == '__main__':
    main()