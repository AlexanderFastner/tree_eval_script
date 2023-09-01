import typer
import sklearn

app = typer.Typer()



#input 2 trees and compute various metrics:silhouette score, Davies bouldin, calinski habermaz


@app.command()
def goodbye(Tree1: str, Tree2: str, height_cutoff: int):
    print(f"Tree1:{Tree1}Tree2:{Tree2}height_cutoff:{height_cutoff}")

if __name__ == "__main__":
    app()
    
    
    
#TODO get 2 example tree files

#implement silhouette score

#implement Davies bouldin
    
#implement calinski habermaz
    
    
#output scores
    
    