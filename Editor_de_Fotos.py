pip instalar travesseiro
# importação de módulos necessários
da importação do tkinter *
de tkinter importar ttk
do tkinter import filedialog
de tkinter.filedialog importar askopenfilename, asksaveasfilename
de PIL importar Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
importar SO
# miniatura de borda de contraste 
raiz = Tk ()
raiz. title ( "Editor de fotos simples" )
raiz. geometria ( "640x640" )
#cria funções
def selecionado () : 
    global img_path, img
    img_path = arquivodialog. askopenfilename ( initialdir = os. getcwd ()) 
    img = imagem. abra ( caminho_img )
    imagem miniatura (( 350 , 350 ))
    #imgg = img.filter(ImageFilter.BoxBlur(0))
    img1 = ImageTk. FotoImagem ( img )
    tela2. create_image ( 300 , 210 , imagem=img1 )
    canvas2.image=img1                                                                                                                                                                                                                
def blur ( evento ) : 
    global img_path, img1, imgg
    para m no intervalo ( 0 , v1. get () + 1 ) : 
            img = imagem. abra ( caminho_img )
            imagem miniatura (( 350 , 350 ))
            img = img. filtro ( ImageFilter. BoxBlur ( m ))
            img1 = ImageTk. FotoImagem ( imgg ) 
            tela2. create_image ( 300 , 210 , imagem=img1 )
            canvas2.image=img1
brilho def ( evento ) : 
    global img_path, img2, img3
    para m no intervalo ( 0 , v2. get () + 1 ) : 
            img = imagem. abra ( caminho_img )
            imagem miniatura (( 350 , 350 ))
            imgg = ImageEnhance. Brilho ( img )
            img2 = img. melhorar ( m )
            img3 = ImageTk. FotoImagem ( img2 )
            tela2. create_image ( 300 , 210 , imagem=img3 )
            canvas2.image=img3
def contraste ( evento ) : 
    global img_path, img4, img5
    para m no intervalo ( 0 , v3. get () + 1 ) : 
            img = imagem. abra ( caminho_img )
            imagem miniatura (( 350 , 350 ))
            imgg = ImageEnhance. Contraste ( img )
            img4 = img. melhorar ( m )
            img5 = ImageTk. FotoImagem ( img4 )
            tela2. create_image ( 300 , 210 , imagem=img5 )
            canvas2.image=img5
def girar_image ( evento ) : 
        global img_path, img6, img7
        img = imagem. abra ( caminho_img )
        imagem miniatura (( 350 , 350 ))
        img6 = img. girar ( int ( girar_combo. get ()))
        img7 = ImageTk. FotoImagem ( img6 )
        tela2. create_image ( 300 , 210 , imagem=img7 )
        canvas2.image=img7
        
def flip_image ( evento ) : 
        global img_path, img8, img9
        img = imagem. abra ( caminho_img )
        imagem miniatura (( 350 , 350 ))
        se flip_combo. get () == "FLIP DA ESQUERDA PARA A DIREITA" :
            img8 = img. transpor ( Image.FLIP_LEFT_RIGHT )
        elif flip_combo. get () == "FLIP TOP TO BOTOM" :
            img8 = img. transpor ( Image.FLIP_TOP_BOTTOM )
        img9 = ImageTk. FotoImagem ( img8 )
        tela2. create_image ( 300 , 210 , imagem=img9 )
        canvas2.image=img9   
def image_border ( evento ) : 
    global img_path, img10, img11
    img = imagem. abra ( caminho_img )
    imagem miniatura (( 350 , 350 ))
    img10 = ImageOps. expand ( img, border= int ( border_combo. get ()) , fill= 95 )
    img11 = ImageTk. FotoImagem ( img10 )
    tela2. create_image ( 300 , 210 , imagem=img11 )
    canvas2.image=img11    
img1 = Nenhum
img3 = Nenhum
img5 = Nenhum
img7 = Nenhum
img9 = Nenhum
img11 = Nenhum
def salvar () : 
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
   #file=Nenhum
    ext = img_path. split ( "." )[ -1 ]
    file= askaveasfilename ( defaultextension =f ".{ext}" ,filetypes= [( "All Files" , "*.*" ) , ( "PNG file" , "*.png" ) , ( "jpg file" , " *.jpg" )])
    se arquivo:
            if canvas2.image==img1:
                imgg. salvar ( arquivo )
            elif canvas2.image==img3:
                img2. salvar ( arquivo )
            elif canvas2.image==img5:
                img4. salvar ( arquivo )
            elif canvas2.image==img7:
                img6. salvar ( arquivo )
            elif canvas2.image==img9:
                img8. salvar ( arquivo )
            elif canvas2.image==img11:
                img10. salvar ( arquivo )        
# cria rótulos, escalas e comboboxes
blurr = Label ( root, text = "Blur:" , font= ( "ariel 17 bold" ) , width= 9 , anchor= 'e' )
borrão. lugar ( x = 15 , y = 8 )
v1 = IntVar ()
escala1 = ttk. Scale ( root, from_= 0 , to= 10 , variable=v1, orient=HORIZONTAL, command=blur ) 
escala1. lugar ( x = 150 , y = 10 )
bright = Label ( root, text = "Brightness:" , font= ( "ariel 17 bold" ))
brilhante. lugar ( x = 8 , y = 50 )
v2 = IntVar ()   
escala2 = ttk. Escala ( root, from_= 0 , to= 10 , variable=v2, orient=HORIZONTAL, command=brightness ) 
escala2. lugar ( x = 150 , y = 55 )
contraste = Label ( root, text = "Contraste:" , font= ( "ariel 17 bold" ))
contraste. lugar ( x = 35 , y = 92 )
v3 = IntVar ()   
escala3 = ttk. Scale ( root, from_= 0 , to= 10 , variable=v3, orient=HORIZONTAL, command=contrast ) 
escala3. lugar ( x = 150 , y = 100 )
girar = Label ( root, text = "Rotate:" , font= ( "ariel 17 bold" ))
girar. lugar ( x = 370 , y = 8 )
valores = [ 0 , 90 , 180 , 270 , 360 ]
girar_combo = ttk. Combobox ( root, values=values, font= ( 'ariel 10 bold' ))
girar_combo. lugar ( x = 460 , y = 15 )
girar_combo. bind ( "<<ComboboxSelected>>" , gira_image )
flip = Label ( root, text = "Flip:" , font = ( "ariel 17 bold" ))
virar. lugar ( x = 400 , y = 50 )
valores1 = [ "FLIP DA ESQUERDA PARA A DIREITA" , "FLIP TOP TO BOTOM" ]
flip_combo = ttk. Combobox ( root, values=values1, font= ( 'ariel 10 bold' ))
flip_combo. lugar ( x = 460 , y = 57 )
flip_combo. bind ( "<<ComboboxSelected>>" , flip_image )
border = Label ( root, text = "Adicionar borda:" , font= ( "ariel 17 bold" ))
fronteira. lugar ( x = 320 , y = 92 )
valores2 = [ i para i no intervalo ( 10 , 45 , 5 )] 
border_combo = ttk. Combobox ( root, values=values2, font= ( "ariel 10 bold" ))
border_combo. lugar ( x = 460 , y = 99 )
border_combo.bind ( "<<ComboboxSelected>>" , image_border )
# cria canvas para exibir a imagem
tela2 = Canvas ( raiz, largura= "600" , altura= "420" , relevo=RIDGE, bd= 2 )
tela2. lugar ( x = 15 , y = 150 )
#criar botões
btn1 = Button ( root, text = "Selecionar Imagem" , bg= 'black' , fg= 'gold' , font= ( 'ariel 15 bold' ) , relevo=GROOVE, command=selected )
btn1. lugar ( x = 100 , y = 595 )
btn2 = Button ( root, text= "Salvar" , largura= 12 , bg= 'black' , fg= 'gold' , font= ( 'ariel 15 bold' ) , relevo=GROOVE, command=save )
btn2. lugar ( x= 280 , y = 595 )
btn3 = Button ( root, text= "Exit" , width= 12 , bg= 'black' , fg= 'gold' , font= ( 'ariel 15 bold' ) , relevo=GROOVE, command=root.destroy )
btn3. lugar ( x = 460 , y = 595 )
raiz. loop principal ()
