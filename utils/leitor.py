def ler_arquivo(caminho):
    with open(caminho, 'r') as f:
        linhas = f.readlines()
        if len(linhas) < 2:
            raise ValueError("O arquivo deve conter ao menos duas linhas: n e nome do algoritmo.")
        
        n = int(linhas[0].strip())
        algoritmo = linhas[1].strip().lower()
        
        if algoritmo not in ["bubblesort", "treesort", "shellsort"]:
            raise ValueError(f"Algoritmo inválido: {algoritmo}")
        
        return n, algoritmo
