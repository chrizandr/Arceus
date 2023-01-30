import json

assigned_prizes = {
    "KOBK": "NidoranM (?) - Level: 4",
    "MIAN": "Shiny/Dark/Normal Snorlax (?) - Level 500",
    "TOOFURIOUZ": "GoldenLucario M - Level: 125",
    "ZZSHADOWZZ": "GoldenRalts M - Level: 4",
    "SOUL CHIMERA": "ShinyEevee F - Level: 5 + Eevee(?) - Level: 4",
    "NEWTON": "Heracross (?) - Level: 500",
    "DEEPAKW": "GoldenVulpix M - Level: 5",
    "LONE": "GoldenRalts (?) - Level: 4",
    "HOODEDFIGURE": "ShinyLucario M - Level: 1025",
    "CHRIS ANDREW": "Arceus - Level: 3002",
    "SHIVA": "4x GoldenPlusle M - Level: 5",
    "KINGCARLOS11": "ShinyDuskull F - Level: 500",
    "THESITUATION": "DarkCharmander F - Level: 7",
    "APATHY": "GoldenSalamence F - Level: 1993 + Salamence (?) - Level: 1999",
    "TEETEN": "10x Mewtwo - Level 500",
    "ELECTROPHORESIS": "Lugia - Level: 2999",
    "GRIFFITH": "ShinyDusclops F - Level: 500",
    "MUMBLES1000": "ShinyPolitoed (?) - Level: 500",
    "NOISIA": "GoldenZapdos - Level: 5",
    "ZAZZ": "Kyurem - Level: 575",
    "DOUBLE_ILLUSION": "GoldenBreloom F - Level: 1999",
    "JUNHAO1806": "Charmander(?) - Level: 20",
    "FUU TAKA": "GoldenRayquaza - Level: 125",
    "TYSONIC": "ShinyUmbreon(?) - Level: 500 + ShinyEspeon F - Level: 500",
    "ACE TRAINER MURDY": "GoldenVulpix M - Level: 7",
    "PLAYAH": "Hoopa (Confined) (Level: 100)",
    "MAGI THE PIRATE": "Shiny/Dark/Normal Snorlax (?) - Level 500",
    "LORDRESHIRAM": "DarkMudkip (?) - Level: 500 + Larvitar (?) - Level: 500",
    "DARK KNIGHT1": "GoldenCranidos M - Level: 5",
    "SAKURA": "Charmander (?) - Level: 500 + DarkMudkip (?) - Level: 500",
    "SANTIE CLAUSE": "ShinyLarvitar (?) - Level: 500",
    "HAUNTER": "Hoopa (Confined) (Level: 100)",
    "1998GAMER": "ShinyAbsol F - Level: 500 + DarkAbsol F - Level: 500",
    "THE STRONG TRAINER": "ShinyHoundour (?) - Level: 505",
    "MCCRAZY": "Mewtwo (?) - Level: 1023",
    "CHUK1996": "Ho-Oh - Level: 3475",
    "PSYCLONE": "ShinyHoundoom (?) - Level: 1000",
    "DOGBONES41": "GoldenMewtwo - Level: 500",
    "MUSTY": "GoldenDratini F - Level: 61",
    "TACHIMUKAI": "ShinyFlareon M - Level: 500",
    "EEVEE": "Ralts (?) - Level: 500",
    "EVERLONG": "GoldenBeldum - Level: 666",
    "SLSAMG": "GoldenMagikarp M - Level: 6",
    "EBADBOY": "DarkCherubi F - Level: 100",
    "LEGEND-KILLER": "DarkCelebi",
    "JOKER_REBORN": "Tyranitar (?) - Level: 56",
    "PKCORE": "GoldenShroomish M - Level: 125",
    "REACTUX": "GoldenGible F - Level: 5",
    "SILENTSWORDSMAN5": "3x ShinyTorkoal (?) - Level: 500",
    "MEWTWO07": "ShinyTogepi (?) - Level: 500",
    "BOSTON2377": "Larvitar (?) - Level: 500",
    "ME FIRST": "GoldenBirdset 5",
    "SPECTRUM": "GoldenRayquaza - Level: 2975",
    "CBOBAND": "GoldenMewtwo - Level: 5",
    "SHAVO": "ShinyDuskull F - Level: 500",
    "DRAGONSLORD": "ShinyEevee M - Level: 400",
    "SHIKIGAMI": "ShinyShinx F - Level: 100",
    "DRAGONEYEZ": "ShinyBreloom M - Level: 3800",
    "NONY7890": "Drowzee (?) - Level: 5",
    "FRANKHUGO": "Heracross (?) - Level: 500 + Houndour(?) - Level: 500",
    "FATE": "Heracross (?) - Level: 500",
    "KEVIZZLE": "DarkAbsol F - Level: 500 + Larvitar(?) - Level: 500",
    "CHARMY": "ShinyClefable M - Level: 500",
    "THANVA": "GoldenArticuno - Level: 5",
    "LORD DEVIL": "Golden Birdset - Level: 5",
    "DROO": "GoldenMagikarp M - Level: 5",
    "HAX": "ShinyScizor (?) - Level: 1040",
    "CYANIDE KISSES": "GoldenMantine (?) - Level: 4",
    "KRISUP": "GoldenGardevoir F - Level: 1000",
    "SYSTEMGHOST": "Beldum (?) - Level: 500",
    "DARKJEWEL": "Larvitar (?) - Level: 500",
    "DRAGONBLADE": "Beldum (?) - Level: 500",
    "CYENSO": "Growlithe (?) - Level: 5",
    "JZ THE CHAMP": "GoldenYanma (?) - Level: 5",
    "ABCODE": "Heracross (?) - Level: 500",
    "ROLEX": "ShinySkarmory (?) - Level: 500",
    "DOSBAYOS": "ShinyLucario F - Level: 1230",
    "TACOBELL1919": "Eevee (?) - Level: 4",
    "DARKGHOST": "ShinyBuneary F - Level: 5",
    "MASTERFRESHIE": "ShinyJirachi - Level: 173 + Latias - Level: 1000 + ShinyPalkia - Level: 125",
    "CHRIS9955": "Bagon (?) - Level: 500",
    "NARCISTIC": "Ho-Oh - Level: 666",
    "PANTHERA LEO": "ShinyLucario M - Level: 99",
    "ABHI": "3x ShinyRiolu",
    "PEPALUS": "GoldenDeino M - Level: 5",
    "FRGT10": "ShinyMewtwo - Level: 329",
    "B0RED": "DarkWobbuffet (?) - Level: 500",
    "PLACEHOLDER": "Mystery prize!",
}


swap_requests = [
    ("B0RED", "EEVEE"),
    ("ZZSHADOWZZ", "PEPALUS"),
    ("SHAVO", "CHUK1996")
]

print("-------------------------------------------------------")
for request in swap_requests:
    p1, p2 = request
    if p1 not in assigned_prizes:
        print(f"Theres no one called {p1}")
        continue
    if p2 not in assigned_prizes:
        print(f"Theres no one called {p2}")
        continue

    print(f"{p1} wants to swap prizes with {p2}")
    prize_p1 = assigned_prizes[p1]
    prize_p2 = assigned_prizes[p2]
    assigned_prizes[p1] = prize_p2
    assigned_prizes[p2] = prize_p1
    print(f"{p1} now has {prize_p2} and {p2} now has {prize_p1}")
    print("-------------------------------------------------------")

print("Final prize list:")
print(json.dumps(assigned_prizes, indent=4))