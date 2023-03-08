import pip

# Modules nécessaires à l'application
required_modules = ['beautifulsoup4', 'fake_useragent', 'matplotlib', 'numpy', 'pandas', 'plotly', 'requests', 'selenium', 'tqdm']

import pkg_resources

def install_missing_packages():
    """Installe les paquets manquants nécessaires à l'application."""
    installed_packages = [d.project_name for d in pkg_resources.working_set]
    packages_to_install = [package for package in required_modules if package not in installed_packages]
    if packages_to_install:
        for package in packages_to_install:
            pip.main(['install', package])
        print('Installation des packages manquants terminée avec succès.')
    else:
        print('Tous les packages nécessaires sont déjà installés.')