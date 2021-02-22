import pokebase as pb


meowth = pb.pokemon("meowth")

for i in range(0, len(meowth.moves)):
    print(meowth.moves[i].move.name + " " +
            meowth.moves[i].version_group_details.level_learned_at)