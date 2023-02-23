import pip

# Modules nécessaires à l'application
required_modules = ['beautifulsoup4', 'fake_useragent', 'matplotlib', 'numpy', 'pandas', 'plotly', 'requests', 'selenium', 'tqdm']

def install_missing_packages():
    """Installe les paquets manquants nécessaires à l'application."""
    installed_packages = pip.get_installed_distributions()
    installed_packages_list = [package.project_name for package in installed_packages]
    packages_to_install = [package for package in required_modules if package not in installed_packages_list]
    if packages_to_install:
        for package in packages_to_install:
            pip.main(['install', package])
        print('Installation des packages manquants terminée avec succès.')
    else:
        print('Tous les packages nécessaires sont déjà installés.')
