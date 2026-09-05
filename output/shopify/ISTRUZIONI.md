# Istruzioni Aggiornamento Tema — Bea & Co.

## Cosa è cambiato
- ✅ **blog.liquid** — Template blog con sidebar e paginazione
- ✅ **article.liquid** — Template articolo con hero image e condivisione
- ✅ **email-popup.liquid** — Popup capture email (mostrato dopo 5s)
- ✅ **header.liquid** — Aggiunto link "Notes" al blog
- ✅ **theme.liquid** — Integrato popup

## Come caricare

### Opzione 1: Upload via Shopify Admin
1. Vai su **Online Store > Temi** nel tuo admin Shopify
2. Clicca **Carica file zip** in alto a destra
3. Seleziona `bea-theme-updated.zip`
4. Clicca **Carica**
5. Attendi il completamento (1-2 minuti)
6. Clicca **Personalizza** per attivare il nuovo tema

### Opzione 2: Upload via Shopify CLI (se installato)
```bash
cd output/shopify/bea-theme
shopify theme push --theme-id=YOUR_THEME_ID
```

### Opzione 3: Copia manualmente
Se hai accesso FTP/SSH al server, carica i file nella cartella del tema.

## Dopo il caricamento

### 1. Crea il Blog
1. Vai su **Articoli > Gestisci blog**
2. Crea un nuovo blog chiamato "Notes" (o "A little clarity")
3. Imposta il handle su `news`

### 2. Pubblica il primo post
1. Vai su **Articoli > Aggiungi articolo**
2. Titolo: "Signs of Separation Anxiety in Dogs: What Most Owners Miss"
3. Contenuto: copia da `Content/Posts/signs-of-separation-anxiety.md`
4. Immagine: usa `bea.jpg` o `guide-cover.png`
5. Tags: separation anxiety, dog anxiety, dog behavior
6. Clicca **Salva** poi **Pubblica**

### 3. Configura Email Capture (Klaviyo/Omnisend)
Vedi `Email-Setup-Guide.md` per i dettagli.

### 4. Testa il popup
1. Vai su bea-co.it
2. Attendi 5 secondi
3. Il popup dovrebbe apparire
4. Inserisci un email di test
5. Verifica che l'email venga catturata

## File ZIP
📦 `output/shopify/bea-theme/bea-theme-updated.zip` (680KB)
