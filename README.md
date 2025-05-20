# LoL_Map_CNN

Set of Algorithms developed in Jupyter Notebook for image recognition regarding League of Legends aftermatch map-playerdeath images.

Multiclass:
- Ind/Role
- Ind+Glob/Role
- Ind/Time
- Glob/Time

Binary:
- Ind/Win
- Glob/Win
- Glob+AllInd/Win

ToDo:
- [General]
    - Resize images to be the same (?)
    - Testar e treinar para intervalos de tempo <30 e <25 min
    - Data Augmentation for Glob pictures
    - Scripts:
        - Image compiler (SingleInd+Glob)(AllInd+Glob)
        - Data Splitter selectable by time

- [RoleDetection]
    - Test different/more paramaters
    - Juntar adc e supp dentro da mesma label
    - Inserir fotos compiladas:
        - Role + global
- [MatchTime]
    -Create
- [SideWin]
    - Test different/more paramaters
    - Compile and test for Glob+AllInd

