import Games_fonction.GameLauch as Fonction
import Games_fonction.Compact_library.Dificult_builder as Dificulty
import Games_fonction.GameUserLibrary.Gamer_Action as Action

a = Action.Chose_type(Fonction.Games_fonction.Compact_library.DATL.List_of_type)
b = Action.Chose_Dificult(Fonction.Games_fonction.Compact_library.DATL.List_of_Dificult)
Fonction.launch_game_with_dificulty(Dificulty.Build_dificulty(a,b))

