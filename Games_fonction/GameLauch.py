import Games_fonction.GameSys
import Games_fonction.Compact_library.Dificult_builder
import Games_fonction.Compact_library.CubeListM
import Games_fonction.GameUserLibrary.GameInSolve
import Games_fonction.Compact_library.DATL

Games_fonction.Compact_library.CubeListM.Get_cube_list(Games_fonction.GameSys)
Games_fonction.Compact_library.CubeListM.MakeCube()
Games_fonction.Compact_library.DATL.Get_Action(Games_fonction.Compact_library.Dificult_builder)
Games_fonction.Compact_library.DATL.Make_Action_List()
def playCube(option):
    while option.life != 0:
        Games_fonction.GameUserLibrary.GameInSolve.cube_info(option)
        option.IncLocalDificult()
        option.DecLife()
        Games_fonction.GameUserLibrary.GameInSolve.To_next_round()
    option.ResetLife()
    option.ResetLocalDificult()
def launch_game_with_dificulty(dificulty_str:str):
    playCube(getattr(Games_fonction.Compact_library.CubeListM, dificulty_str))