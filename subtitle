#!/bin/bash

# Vérifier si autosrt est installé
if ! command -v autosrt &> /dev/null; then
    echo "Le programme autosrt n'est pas installé. Veuillez l'installer avant de continuer."
    exit 1
fi

# Demander à l'utilisateur le chemin de la vidéo
read -p "Veuillez entrer le chemin de votre vidéo : " video_path

# Vérifier si le fichier vidéo existe
if [ ! -f "Input_videos/${video_path}" ]; then
    echo "Le fichier vidéo n'existe pas. Veuillez vérifier le chemin et réessayer."
    exit 1
fi

# Lire la langue des sous-titres à partir du fichier langue.txt
lang=$(cat langue.txt)
echo $lang;

# Utiliser autosrt pour générer les sous-titres avec la langue spécifiée
autosrt -S $lang "Input_videos/${video_path}"

# Vérifier si la génération des sous-titres a réussi
if [ $? -eq 0 ]; then
    echo "Sous-titres générés avec succès."
else
    echo "Échec de la génération des sous-titres."
    exit 1
fi
