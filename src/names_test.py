from names import *

def main():
    names_freq = read_names_freq("./data/frecuencias_nombres.csv")
    print(f"we have {len(names_freq)} names frequency")
    print(f"First name and year {names_freq[0]}")

    male_freqs = filter_gender(names_freq, "Hombre")
    print(f"Hay una frecuencia de {len(male_freqs)} nombres")
    name_woman = get_names(names_freq, "Mujer")
    print(f"Hay {len(name_woman)}")
    freq_name_per_year = got_top_n_year(names_freq, 2017)
    print(freq_name_per_year)
    selec = get_common_names(names_freq)
    print(selec)

    print(get_compound_names(names_freq))
    most_commons_names_per_year(names_freq)
    show_evolution_year(names_freq, "HUGO")

if __name__ == "__main__":
    main()