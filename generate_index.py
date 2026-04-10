import os

def generate_index():
    # Obtener todos los archivos .html en la carpeta actual, excluyendo index.html
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.html') and f != 'index.html']
    
    # Ordenar alfabéticamente
    files.sort()

    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Índice de Prototipos - Beta Freight</title>
    <style>
        :root {
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --bg: #f1f5f9;
            --text: #0f172a;
            --card-bg: #ffffff;
            --border: #e2e8f0;
        }
        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            max-width: 1000px;
            margin: 40px auto;
            padding: 0 20px;
            line-height: 1.5;
        }
        header {
            text-align: center;
            margin-bottom: 50px;
        }
        h1 {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 8px;
            font-weight: 800;
        }
        p {
            color: #64748b;
            font-size: 1.1rem;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 24px;
        }
        .card {
            background: var(--card-bg);
            padding: 24px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none;
            display: flex;
            flex-direction: column;
            border: 1px solid var(--border);
        }
        .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
            border-color: var(--primary);
        }
        .card-title {
            font-weight: 700;
            font-size: 1.25rem;
            color: var(--text);
            margin-bottom: 8px;
            text-transform: capitalize;
        }
        .card-path {
            font-size: 0.875rem;
            color: #64748b;
            font-family: 'Cascadia Code', 'Fira Code', monospace;
            background: #f8fafc;
            padding: 4px 8px;
            border-radius: 6px;
            word-break: break-all;
        }
        .status {
            margin-top: 16px;
            display: inline-flex;
            align-items: center;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--primary);
        }
        .status::before {
            content: "";
            display: inline-block;
            width: 8px;
            height: 8px;
            background-color: var(--primary);
            border-radius: 50%;
            margin-right: 8px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Beta Freight</h1>
        <p>Listado automático de prototipos y vistas</p>
    </header>
    <div class="grid">
"""

    for file in files:
        # Formatear el nombre: quitar .html, cambiar guiones/puntos por espacios y capitalizar
        name = file.replace('.html', '').replace('_', ' ').replace('-', ' ')
        html_content += f"""        <a href="{file}" class="card">
            <span class="card-title">{name}</span>
            <span class="card-path">{file}</span>
            <div class="status">Vista HTML</div>
        </a>\n"""

    html_content += """    </div>
    <footer style="margin-top: 60px; text-align: center; color: #94a3b8; font-size: 0.875rem;">
        Generado automáticamente por generate_index.py
    </footer>
</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Se ha generado 'index.html' con {len(files)} archivos encontrados.")

if __name__ == "__main__":
    generate_index()
