# HTML-Clones

Proiectul detectează paginile HTML similare dintr-un director dat, pe care le grupează pe baza similarității textului, a tag-urilor și a structurii DOM.


    ```bash
    git clone https://github.com/bianca9944/HTML-Clones.git
    ```
    
    ```bash
    pip install -r requirements.txt
    ```

```bash
python main.py /bianca9944/HTML-Clones/blob/main/main.py

python main.py /bianca9944/HTML-Clones/blob/main/main.py --threshold 0.7 --weight_text 0.6 --weight_dom 0.2 --weight_tag 0.2
