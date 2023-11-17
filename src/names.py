import csv
from typing import NamedTuple, List, Optional, Set, Tuple, Dict
from collections import defaultdict
import matplotlib.pyplot as plt

NameFreq = NamedTuple("NameFreq",[("year",int),("name",str),("frequency", int),("gender",str)])


#EXCERCISE 1    
def read_names_freq(filename:str) -> List[NameFreq]:
    with open(filename) as file:
        archivo = csv.reader(file)
        next(archivo)
        lista = [NameFreq(int(year),name,int(frequency),gender) for year,name,frequency,gender in archivo]
        return lista

#EXCERCISE 2
def filter_gender(names: List[NameFreq], g:str) -> List[NameFreq]:
    if g in ["Hombre", "Mujer"]:
        return [s for s in names if s.gender == g]
    

#EXCERCISE 3
def get_names(names: List[NameFreq], g:Optional[str]=None) -> Set[str]:
    return {s.name for s in names if g==None or s.gender==g}
    
#EXERCISE 4
def got_top_n_year(names: List[NameFreq], year: int, limit:int=10, g:Optional[str]=None) -> List[Tuple[str,int]]:
    #SELECT TUPLES ACCORDING TO YEAR AND GENDER
    selection = [s for s in names if s.year == year and (g==None or s.gender==g)]
    #SORT TUPLES ACCORDING TO FREQUENCY
    selection.sort(key=lambda a:a.frequency, reverse=True)
    #CREATE LIST OF TUPLES OF THE FIRST LIMIT
    #return selection[:limit]
    return [(s.name, s.frequency) for s in selection][:limit]

#EX 5
def get_common_names(names: List[NameFreq]) -> Set[str]:
    man_names = {s.name for s in names if s.gender=="Hombre"}
    woman_names = {s.name for s in names if s.gender=="Mujer"}
    return man_names & woman_names

#EX 6
def get_compound_names(names:List[NameFreq], g:Optional[str]=None) -> Set[str]:
    return {s.name for s in names if ' ' in s.name and (g==None or g==s.gender)}

#EX 7
def most_commons_names_per_year(names:List[NameFreq]):
    dic = defaultdict(list)
    for s in names:
        year = s.year
        dic[year].append((s.name, s.frequency))
    orden = sorted(dic.items(),key=lambda x:x[1][1][1], reverse=True)
    for s in orden:
        print(s[0], s[1][1][0])
    return orden


#EX 8
def get_year_frequencies(names: List[NameFreq], name: str) -> List[Tuple[int,int]]:
    d = defaultdict(int)
    for s in names:
        if s.name == name:
            d[s.year] += s.frequency
    return sorted(d.items())


def show_evolution_year(names: List[NameFreq], name:str) ->None:
    year, freq = zip(*get_year_frequencies(names, name))
    plt.plot(year, freq)
    plt.title(f"Evolición nombre {name}")
    plt.show()
