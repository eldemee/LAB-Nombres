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
def most_commons_names_per_year(names:List[NameFreq]) -> List[Tuple[int, str]]:
    dic = defaultdict(list)
    for s in names:
        year = s.year
        dic[year].append((s.name, s.frequency))
    frequency = [(s[0], s[1][1][0]) for s in dic.items()]
    return frequency


#EX 8
def get_year_frequencies(names: List[NameFreq], name: str) -> List[Tuple[int,int]]:
    d = defaultdict(int)
    for s in names:
        if s.name == name:
            d[s.year] += s.frequency
    return sorted(d.items())

#EX 9
def show_evolution_year(names: List[NameFreq], name:List) ->None:
    for n in name: 
        year, freq = zip(*get_year_frequencies(names, n))
        plt.plot(year, freq)
        plt.title(f"Evolición nombre {n}")
        plt.show()

#EX 11 AND 12
def get_freq_by_names(names: List[NameFreq]) -> Dict[str, int]:
    d = {}
    nombres = {e.name for e in names}
    for name in nombres:
        d[name] = acumulated_frequency(names, name)
    return d


def acumulated_frequency(names: List[NameFreq], n: str) -> int:
    return sum(name.frequency for name in names if n==name.name)
    

#EX 12
def show_names_freqs(names: List[NameFreq], limit:int=10) -> None:
    acumulated_frequency = sorted(get_freq_by_names(names).items(), key=lambda n:n[1], reverse=True )[:limit]
    nombres, freq = zip(*acumulated_frequency)

    plt.bar(nombres, freq)
    plt.xticks(rotation = 80)
    plt.title(f"Top {limit} nombres mas comunes")
    plt.show()
