from django.db import models  # Importation du module models de Django pour créer des modèles de base de données

# Création des modèles ici

class StudentInfo(models.Model):  # Modèle pour stocker les informations des étudiants
    code_module = models.CharField(max_length=45)  # Code du module, chaîne de caractères de longueur maximale 45
    code_presentation = models.CharField(max_length=45)  # Code de la présentation, chaîne de caractères de longueur maximale 45
    id_student = models.IntegerField()  # Identifiant de l'étudiant, entier
    gender = models.CharField(max_length=3)  # Genre de l'étudiant, chaîne de caractères de longueur maximale 3
    imd_band = models.CharField(max_length=16, null=True)  # Bande IMD, chaîne de caractères de longueur maximale 16, peut être null
    highest_education = models.CharField(max_length=45, null=True)  # Niveau d'éducation le plus élevé, chaîne de caractères de longueur maximale 45, peut être null
    age_band = models.CharField(max_length=16, null=True)  # Tranche d'âge, chaîne de caractères de longueur maximale 16, peut être null
    num_of_prev_attempts = models.IntegerField(null=True)  # Nombre de tentatives précédentes, entier, peut être null
    studied_credits = models.IntegerField(null=True)  # Crédits étudiés, entier, peut être null
    region = models.CharField(max_length=45, null=True)  # Région, chaîne de caractères de longueur maximale 45, peut être null
    disability = models.CharField(max_length=3, null=True)  # Handicap, chaîne de caractères de longueur maximale 3, peut être null
    final_result = models.CharField(max_length=45, null=True)  # Résultat final, chaîne de caractères de longueur maximale 45, peut être null

    def __str__(self):  # Méthode pour représenter l'objet sous forme de chaîne
        return f'{self.id_student} - {self.final_result}'  # Retourne l'identifiant de l'étudiant et le résultat final

class StudentRegistration(models.Model):  # Modèle pour stocker les informations d'inscription des étudiants
    code_module = models.CharField(max_length=45)  # Code du module, chaîne de caractères de longueur maximale 45
    code_presentation = models.CharField(max_length=45)  # Code de la présentation, chaîne de caractères de longueur maximale 45
    id_student = models.IntegerField()  # Identifiant de l'étudiant, entier
    date_registration = models.IntegerField()  # Date d'inscription, entier
    date_unregistration = models.IntegerField(null=True, blank=True)  # Date de désinscription, entier, peut être null et vide

    def __str__(self):  # Méthode pour représenter l'objet sous forme de chaîne
        return f'{self.id_student} - {self.code_module}'  # Retourne l'identifiant de l'étudiant et le code du module

class StudentAssessment(models.Model):  # Modèle pour stocker les informations d'évaluation des étudiants
    id_student = models.IntegerField()  # Identifiant de l'étudiant, entier
    id_assessment = models.IntegerField()  # Identifiant de l'évaluation, entier
    date_submitted = models.IntegerField()  # Date de soumission, entier
    is_banked = models.BooleanField(default=False)  # Indique si l'évaluation est en banque, booléen avec valeur par défaut False
    score = models.FloatField(null=True)  # Score de l'évaluation, flottant, peut être null

    def __str__(self):  # Méthode pour représenter l'objet sous forme de chaîne
        return f'{self.id_student} - {self.id_assessment}'  # Retourne l'identifiant de l'étudiant et l'identifiant de l'évaluation

class Assessments(models.Model):  # Modèle pour stocker les informations des évaluations
    code_module = models.CharField(max_length=45)  # Code du module, chaîne de caractères de longueur maximale 45
    code_presentation = models.CharField(max_length=45)  # Code de la présentation, chaîne de caractères de longueur maximale 45
    id_assessment = models.IntegerField()  # Identifiant de l'évaluation, entier
    assessment_type = models.CharField(max_length=45)  # Type d'évaluation, chaîne de caractères de longueur maximale 45
    date = models.IntegerField()  # Date de l'évaluation, entier

    def __str__(self):  # Méthode pour représenter l'objet sous forme de chaîne
        return f'{self.id_assessment} - {self.assessment_type}'  # Retourne l'identifiant de l'évaluation et le type d'évaluation

class Courses(models.Model):  # Modèle pour stocker les informations des cours
    code_module = models.CharField(max_length=45)  # Code du module, chaîne de caractères de longueur maximale 45
    code_presentation = models.CharField(max_length=45)  # Code de la présentation, chaîne de caractères de longueur maximale 45

    def __str__(self):  # Méthode pour représenter l'objet sous forme de chaîne
        return f'{self.code_module} - {self.code_presentation}'  # Retourne le code du module et le code de la présentation

class Vle(models.Model):  # Modèle pour stocker les informations des environnements d'apprentissage virtuels
    id_site = models.IntegerField()  # Identifiant du site, entier
    code_module = models.CharField(max_length=45)  # Code du module, chaîne de caractères de longueur maximale 45
    code_presentation = models.CharField(max_length=45)  # Code de la présentation, chaîne de caractères de longueur maximale 45
    activity_type = models.CharField(max_length=45)  # Type d'activité, chaîne de caractères de longueur maximale 45
    week_from = models.IntegerField()  # Semaine de début, entier
    week_to = models.IntegerField()  # Semaine de fin, entier

    def __str__(self):  # Méthode pour représenter l'objet sous forme de chaîne
        return f'{self.id_site} - {self.activity_type}'  # Retourne l'identifiant du site et le type d'activité

class StudentVle(models.Model):  # Modèle pour stocker les interactions des étudiants avec les environnements d'apprentissage virtuels
    id_site = models.IntegerField()  # Identifiant du site, entier
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)  # Référence à l'étudiant, clé étrangère vers StudentInfo, suppression en cascade
    code_module = models.CharField(max_length=45)  # Code du module, chaîne de caractères de longueur maximale 45
    code_presentation = models.CharField(max_length=45)  # Code de la présentation, chaîne de caractères de longueur maximale 45
    date = models.IntegerField()  # Date de l'interaction, entier
    sum_click = models.IntegerField(null=True)  # Nombre de clics, entier, peut être null

    def __str__(self):  # Méthode pour représenter l'objet sous forme de chaîne
        return f'{self.student} - {self.id_site}'  # Retourne l'étudiant et l'identifiant du site
