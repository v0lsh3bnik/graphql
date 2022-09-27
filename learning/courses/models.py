# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutoAttestation(models.Model):
    numero = models.BigIntegerField(unique=True)
    disponible = models.BooleanField()
    observation = models.CharField(max_length=255, blank=True, null=True)
    carnet = models.ForeignKey('AutoCarnet', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auto_attestation'


class AutoCarnet(models.Model):
    typecarnet = models.CharField(db_column='typeCarnet', max_length=10)  # Field name made lowercase.
    reference = models.CharField(max_length=50)
    numerodebut = models.BigIntegerField(db_column='numeroDebut')  # Field name made lowercase.
    numerofin = models.BigIntegerField(db_column='numeroFin')  # Field name made lowercase.
    nombreattestation = models.SmallIntegerField(db_column='nombreAttestation')  # Field name made lowercase.
    dateacquisition = models.DateField(db_column='dateAcquisition')  # Field name made lowercase.
    dateouverture = models.DateField(db_column='dateOuverture')  # Field name made lowercase.
    datefermeture = models.DateField(db_column='dateFermeture')  # Field name made lowercase.
    observation = models.CharField(max_length=255, blank=True, null=True)
    compagnie = models.ForeignKey('ParametreCompagnie', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auto_carnet'


class AutoEnergie(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_energie'


class AutoGenre(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_genre'


class AutoInventaire(models.Model):
    dateinventaire = models.DateField(db_column='dateInventaire')  # Field name made lowercase.
    observation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_inventaire'


class AutoInventairedetails(models.Model):
    observation = models.CharField(max_length=255, blank=True, null=True)
    attestation = models.ForeignKey(AutoAttestation, models.DO_NOTHING)
    inventaire = models.ForeignKey(AutoInventaire, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auto_inventairedetails'


class AutoMarque(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_marque'


class AutoPerte(models.Model):
    dateperte = models.DateField(db_column='datePerte')  # Field name made lowercase.
    typeperte = models.CharField(db_column='typePerte', max_length=1)  # Field name made lowercase.
    observation = models.CharField(max_length=255, blank=True, null=True)
    attestation = models.ForeignKey(AutoAttestation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auto_perte'


class AutoPuissance(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_puissance'


class AutoTarification(models.Model):
    tarif = models.IntegerField()
    branche = models.ForeignKey('ParametreBranche', models.DO_NOTHING)
    compagnie = models.ForeignKey('ParametreCompagnie', models.DO_NOTHING)
    garantie = models.ForeignKey('ParametreGarantie', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auto_tarification'


class AutoTypevehicule(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_typevehicule'


class AutoTypezone(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_typezone'


class AutoUsage(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_usage'


class AutoVehicule(models.Model):
    garantie = models.CharField(max_length=1)
    primenette = models.FloatField(db_column='primeNette')  # Field name made lowercase.
    typevehicule = models.CharField(db_column='typeVehicule', max_length=50, blank=True, null=True)  # Field name made lowercase.
    immatriculation = models.CharField(max_length=20)
    anneemec = models.DateField(db_column='anneeMEC')  # Field name made lowercase.
    chargeutile = models.FloatField(db_column='chargeUtile')  # Field name made lowercase.
    valeurneuve = models.IntegerField(db_column='valeurNeuve')  # Field name made lowercase.
    valeurvenale = models.IntegerField(db_column='valeurVenale')  # Field name made lowercase.
    remorque = models.CharField(max_length=20)
    immatriculationremorque = models.CharField(db_column='immatriculationRemorque', max_length=255)  # Field name made lowercase.
    chargeutileremorque = models.FloatField(db_column='chargeUtileRemorque')  # Field name made lowercase.
    nombreplace = models.SmallIntegerField(db_column='nombrePlace')  # Field name made lowercase.
    assure = models.CharField(max_length=255)
    immatriculationancienne = models.CharField(db_column='immatriculationAncienne', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cylindre = models.IntegerField()
    primerc = models.FloatField(db_column='primeRC')  # Field name made lowercase.
    fondgarantie = models.FloatField(db_column='fondGarantie')  # Field name made lowercase.
    cartebrune = models.FloatField(db_column='carteBrune')  # Field name made lowercase.
    primettc = models.FloatField(db_column='primeTTC')  # Field name made lowercase.
    retrait = models.BooleanField()
    actif = models.BooleanField()
    photo = models.CharField(max_length=100, blank=True, null=True)
    avenant = models.ForeignKey('ParametreAvenant', models.DO_NOTHING)
    energie = models.ForeignKey(AutoEnergie, models.DO_NOTHING)
    genre = models.ForeignKey(AutoGenre, models.DO_NOTHING)
    marque = models.ForeignKey(AutoMarque, models.DO_NOTHING)
    puissance = models.ForeignKey(AutoPuissance, models.DO_NOTHING)
    usage = models.ForeignKey(AutoUsage, models.DO_NOTHING)
    attcedeao = models.BigIntegerField(db_column='attCEDEAO')  # Field name made lowercase.
    attnumero = models.BigIntegerField(db_column='attNumero')  # Field name made lowercase.
    attestationnumero = models.BigIntegerField(db_column='attestationNumero')  # Field name made lowercase.
    attestationcedeao = models.BigIntegerField(db_column='attestationCEDEAO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auto_vehicule'


class AutoVehiculetampon(models.Model):
    garantie = models.CharField(max_length=1)
    primenette = models.FloatField(db_column='primeNette')  # Field name made lowercase.
    typevehicule = models.CharField(db_column='typeVehicule', max_length=50)  # Field name made lowercase.
    immatriculation = models.CharField(max_length=20)
    anneemec = models.DateField(db_column='anneeMEC')  # Field name made lowercase.
    chargeutile = models.FloatField(db_column='chargeUtile')  # Field name made lowercase.
    valeurneuve = models.IntegerField(db_column='valeurNeuve')  # Field name made lowercase.
    valeurvenale = models.IntegerField(db_column='valeurVenale')  # Field name made lowercase.
    remorque = models.CharField(max_length=20)
    immatriculationremorque = models.CharField(db_column='immatriculationRemorque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chargeutileremorque = models.FloatField(db_column='chargeUtileRemorque')  # Field name made lowercase.
    nombreplace = models.SmallIntegerField(db_column='nombrePlace')  # Field name made lowercase.
    attestationnumero = models.CharField(db_column='attestationNumero', max_length=20)  # Field name made lowercase.
    attestationcedeao = models.CharField(db_column='attestationCEDEAO', max_length=20)  # Field name made lowercase.
    assure = models.CharField(max_length=255)
    immatriculationancienne = models.CharField(db_column='immatriculationAncienne', max_length=20)  # Field name made lowercase.
    cylindre = models.IntegerField()
    primerc = models.FloatField(db_column='primeRC')  # Field name made lowercase.
    fondgarantie = models.FloatField(db_column='fondGarantie')  # Field name made lowercase.
    cartebrune = models.FloatField(db_column='carteBrune')  # Field name made lowercase.
    primettc = models.FloatField(db_column='primeTTC')  # Field name made lowercase.
    retrait = models.BooleanField()
    photo = models.CharField(max_length=100, blank=True, null=True)
    avenant = models.ForeignKey('ParametreAvenant', models.DO_NOTHING)
    energie = models.ForeignKey(AutoEnergie, models.DO_NOTHING)
    genre = models.ForeignKey(AutoGenre, models.DO_NOTHING)
    marque = models.ForeignKey(AutoMarque, models.DO_NOTHING)
    puissance = models.ForeignKey(AutoPuissance, models.DO_NOTHING)
    usage = models.ForeignKey(AutoUsage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auto_vehiculetampon'


class AutoVoiture(models.Model):
    garantie = models.CharField(max_length=1)
    primenette = models.IntegerField(db_column='primeNette')  # Field name made lowercase.
    typevehicule = models.CharField(db_column='typeVehicule', max_length=50)  # Field name made lowercase.
    immatriculation = models.CharField(max_length=20)
    anneemec = models.DateField(db_column='anneeMEC')  # Field name made lowercase.
    chargeutile = models.FloatField(db_column='chargeUtile')  # Field name made lowercase.
    valeurneuve = models.IntegerField(db_column='valeurNeuve')  # Field name made lowercase.
    valeurvenale = models.IntegerField(db_column='valeurVenale')  # Field name made lowercase.
    remorque = models.CharField(max_length=20)
    immatriculationremorque = models.CharField(db_column='immatriculationRemorque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chargeutileremorque = models.IntegerField(db_column='chargeUtileRemorque')  # Field name made lowercase.
    nombreplace = models.SmallIntegerField(db_column='nombrePlace')  # Field name made lowercase.
    attestationnumero = models.CharField(db_column='attestationNumero', max_length=20)  # Field name made lowercase.
    attestationcedeao = models.CharField(db_column='attestationCEDEAO', max_length=20)  # Field name made lowercase.
    assure = models.CharField(max_length=255)
    immatriculationancienne = models.CharField(db_column='immatriculationAncienne', max_length=20)  # Field name made lowercase.
    cylindre = models.IntegerField()
    primerc = models.IntegerField(db_column='primeRC')  # Field name made lowercase.
    fondgarantie = models.IntegerField(db_column='fondGarantie')  # Field name made lowercase.
    cartebrune = models.IntegerField(db_column='carteBrune')  # Field name made lowercase.
    primettc = models.IntegerField(db_column='primeTTC')  # Field name made lowercase.
    retrait = models.BooleanField()
    actif = models.BooleanField()
    photo = models.CharField(max_length=100, blank=True, null=True)
    avenant = models.ForeignKey('ParametreAvenant', models.DO_NOTHING)
    energie = models.ForeignKey(AutoEnergie, models.DO_NOTHING)
    genre = models.ForeignKey(AutoGenre, models.DO_NOTHING)
    marque = models.ForeignKey(AutoMarque, models.DO_NOTHING)
    puissance = models.ForeignKey(AutoPuissance, models.DO_NOTHING)
    usage = models.ForeignKey(AutoUsage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auto_voiture'


class AutoZone(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)
    typezone = models.ForeignKey(AutoTypezone, models.DO_NOTHING, db_column='typeZone_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auto_zone'


class CotationCotationaccessoire(models.Model):
    id = models.BigAutoField(primary_key=True)
    formule = models.CharField(max_length=1)
    periode = models.SmallIntegerField()
    compagnie = models.ForeignKey('ParametreCompagnie', models.DO_NOTHING)
    montant = models.SmallIntegerField()
    taux = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cotation_cotationaccessoire'


class CotationCotationflotte(models.Model):
    id = models.BigAutoField(primary_key=True)
    categorie_socio_professionnelle = models.CharField(max_length=20)
    type_cotation = models.CharField(max_length=1)
    transformee = models.BooleanField()
    compagnie = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    police_provisoire = models.CharField(max_length=10)
    primenette = models.FloatField(db_column='primeNette')  # Field name made lowercase.
    accessoire = models.FloatField()
    taxe = models.FloatField()
    fondgarantie = models.FloatField(db_column='fondGarantie')  # Field name made lowercase.
    cartebrune = models.FloatField(db_column='carteBrune')  # Field name made lowercase.
    primettc = models.FloatField(db_column='primeTTC')  # Field name made lowercase.
    civilite = models.ForeignKey('ParametreCivilite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cotation_cotationflotte'


class CotationCotationmatrice(models.Model):
    id = models.BigAutoField(primary_key=True)
    categorie = models.CharField(max_length=255)
    formule = models.CharField(max_length=1)
    garantie = models.CharField(max_length=50)
    socio_professionnelle = models.BooleanField()
    bns = models.BooleanField()
    commerciale = models.BooleanField()
    compagnie = models.ForeignKey('ParametreCompagnie', models.DO_NOTHING)
    montant = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cotation_cotationmatrice'
        unique_together = (('compagnie', 'categorie', 'formule', 'garantie'),)


class CotationCotationrc(models.Model):
    id = models.BigAutoField(primary_key=True)
    categorie = models.CharField(max_length=255)
    formule = models.CharField(max_length=1)
    energie = models.CharField(max_length=10)
    puissance = models.CharField(max_length=3)
    montant = models.IntegerField()
    compagnie = models.ForeignKey('ParametreCompagnie', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cotation_cotationrc'


class CotationCotationsauvegarde(models.Model):
    id = models.BigAutoField(primary_key=True)
    compagnie = models.ForeignKey('ParametreCompagnie', models.DO_NOTHING)
    utilisateur = models.CharField(max_length=50)
    date_cotation = models.DateField()
    contenu = models.TextField()
    profil = models.ForeignKey('ParametreProfil', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cotation_cotationsauvegarde'


class CotationCotationtamponsauvegarde(models.Model):
    id = models.BigAutoField(primary_key=True)
    utilisateur = models.CharField(max_length=50)
    date_cotation = models.DateField()
    contenu = models.TextField()

    class Meta:
        managed = False
        db_table = 'cotation_cotationtamponsauvegarde'


class CotationCotationtaux(models.Model):
    id = models.BigAutoField(primary_key=True)
    taux_socio = models.FloatField()
    taux_bns = models.FloatField()
    taux_commercial = models.FloatField()
    taux_flotte = models.FloatField()
    taux_taxe = models.FloatField()
    taux_fond_garantie = models.FloatField()
    carte_brune = models.IntegerField()
    compagnie = models.OneToOneField('ParametreCompagnie', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cotation_cotationtaux'


class CotationDevis1(models.Model):
    id = models.BigAutoField(primary_key=True)
    categorie = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cotation_devis1'


class CotationDevis2(models.Model):
    id = models.BigAutoField(primary_key=True)
    immatriculation = models.CharField(max_length=255)
    date_mec = models.DateField()
    place = models.SmallIntegerField()
    cylindre = models.SmallIntegerField()
    numero_chassis = models.CharField(max_length=255)
    valeur_neuve = models.IntegerField()
    valeur_venale = models.IntegerField()
    charge_utile = models.IntegerField()
    energie = models.ForeignKey(AutoEnergie, models.DO_NOTHING)
    marque = models.ForeignKey(AutoMarque, models.DO_NOTHING)
    puissance = models.ForeignKey(AutoPuissance, models.DO_NOTHING)
    genre = models.ForeignKey(AutoGenre, models.DO_NOTHING)
    usage = models.ForeignKey(AutoUsage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cotation_devis2'


class CotationDevis3(models.Model):
    id = models.BigAutoField(primary_key=True)
    formule = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cotation_devis3'


class CotationDevis4(models.Model):
    id = models.BigAutoField(primary_key=True)
    periode_couverture = models.CharField(max_length=255)
    periode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cotation_devis4'


class CotationDevis5(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    civilite = models.ForeignKey('ParametreCivilite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cotation_devis5'


class CotationFacturation(models.Model):
    id = models.BigAutoField(primary_key=True)
    categorie = models.CharField(max_length=255)
    charge_utile = models.IntegerField()
    civilite = models.ForeignKey('ParametreCivilite', models.DO_NOTHING)
    compagnie = models.CharField(max_length=255, blank=True, null=True)
    cylindre = models.SmallIntegerField(blank=True, null=True)
    date_mec = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    energie = models.ForeignKey(AutoEnergie, models.DO_NOTHING)
    formule = models.CharField(max_length=255)
    immatriculation = models.CharField(max_length=255, blank=True, null=True)
    marque = models.ForeignKey(AutoMarque, models.DO_NOTHING)
    nom = models.CharField(max_length=255)
    numero = models.CharField(max_length=20, blank=True, null=True)
    numero_chassis = models.CharField(max_length=255, blank=True, null=True)
    periode = models.IntegerField(blank=True, null=True)
    periode_couverture = models.CharField(max_length=255)
    place = models.SmallIntegerField(blank=True, null=True)
    police_provisoire = models.CharField(max_length=20, blank=True, null=True)
    prenoms = models.CharField(max_length=255, blank=True, null=True)
    puissance = models.ForeignKey(AutoPuissance, models.DO_NOTHING)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    transformee = models.BooleanField()
    type_cotation = models.CharField(max_length=1)
    valeur_neuve = models.IntegerField()
    valeur_venale = models.IntegerField()
    genre = models.ForeignKey(AutoGenre, models.DO_NOTHING)
    usage = models.ForeignKey(AutoUsage, models.DO_NOTHING)
    primenette = models.FloatField(db_column='primeNette')  # Field name made lowercase.
    accessoire = models.FloatField()
    cartebrune = models.FloatField(db_column='carteBrune')  # Field name made lowercase.
    fondgarantie = models.FloatField(db_column='fondGarantie')  # Field name made lowercase.
    primettc = models.FloatField(db_column='primeTTC')  # Field name made lowercase.
    taxe = models.FloatField()
    profil = models.ForeignKey('ParametreProfil', models.DO_NOTHING)
    structure = models.CharField(max_length=20)
    categorie_socio_professionnelle = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cotation_facturation'


class CotationVehiculeflotte(models.Model):
    id = models.BigAutoField(primary_key=True)
    categorie = models.CharField(max_length=255)
    immatriculation = models.CharField(max_length=255, blank=True, null=True)
    date_mec = models.DateField()
    place = models.SmallIntegerField(blank=True, null=True)
    cylindre = models.SmallIntegerField(blank=True, null=True)
    numero_chassis = models.CharField(max_length=255)
    valeur_neuve = models.IntegerField(blank=True, null=True)
    valeur_venale = models.IntegerField(blank=True, null=True)
    charge_utile = models.IntegerField(blank=True, null=True)
    formule = models.CharField(max_length=255)
    periode_couverture = models.CharField(max_length=255)
    periode = models.IntegerField()
    primenette = models.FloatField(db_column='primeNette')  # Field name made lowercase.
    accessoire = models.FloatField()
    taxe = models.FloatField()
    fondgarantie = models.FloatField(db_column='fondGarantie')  # Field name made lowercase.
    cartebrune = models.FloatField(db_column='carteBrune')  # Field name made lowercase.
    primettc = models.FloatField(db_column='primeTTC')  # Field name made lowercase.
    cotationflotte = models.ForeignKey(CotationCotationflotte, models.DO_NOTHING)
    energie = models.ForeignKey(AutoEnergie, models.DO_NOTHING)
    marque = models.ForeignKey(AutoMarque, models.DO_NOTHING)
    puissance = models.ForeignKey(AutoPuissance, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cotation_vehiculeflotte'


class DevisflotteCotationaccessoire(models.Model):
    id = models.BigAutoField(primary_key=True)
    cie = models.CharField(max_length=50)
    periode = models.SmallIntegerField()
    montant = models.FloatField()

    class Meta:
        managed = False
        db_table = 'devisflotte_cotationaccessoire'
        unique_together = (('cie', 'periode'),)


class DevisflotteCotationparametre(models.Model):
    id = models.BigAutoField(primary_key=True)
    cie = models.CharField(max_length=50)
    gtie = models.CharField(max_length=100)
    c1 = models.FloatField()
    c2 = models.FloatField()
    c3 = models.FloatField()
    c4 = models.FloatField()
    socio = models.BooleanField()
    bns = models.BooleanField()
    commercial = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'devisflotte_cotationparametre'
        unique_together = (('cie', 'gtie'),)


class DevisflotteDetailsflotte(models.Model):
    id = models.BigAutoField(primary_key=True)
    categorie = models.CharField(max_length=255)
    immatriculation = models.CharField(max_length=255, blank=True, null=True)
    date_mec = models.DateField()
    cylindre = models.SmallIntegerField(blank=True, null=True)
    place = models.SmallIntegerField(blank=True, null=True)
    numero_chassis = models.CharField(max_length=255)
    valeur_neuve = models.IntegerField(blank=True, null=True)
    valeur_venale = models.IntegerField(blank=True, null=True)
    charge_utile = models.IntegerField(blank=True, null=True)
    formule = models.CharField(max_length=255)
    devisflotte = models.ForeignKey('DevisflotteDevisflotte', models.DO_NOTHING)
    energie = models.ForeignKey(AutoEnergie, models.DO_NOTHING)
    marque = models.ForeignKey(AutoMarque, models.DO_NOTHING)
    puissance = models.ForeignKey(AutoPuissance, models.DO_NOTHING)
    genre = models.ForeignKey(AutoGenre, models.DO_NOTHING)
    usage = models.ForeignKey(AutoUsage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'devisflotte_detailsflotte'


class DevisflotteDevisflotte(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_cotation = models.CharField(max_length=1)
    transformee = models.BooleanField()
    compagnie = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    numero = models.CharField(max_length=15)
    police_provisoire = models.CharField(max_length=15)
    date_devis = models.DateField()
    periode_couverture = models.CharField(max_length=255)
    bns_annee = models.SmallIntegerField(blank=True, null=True)
    taux_commercial = models.SmallIntegerField(blank=True, null=True)
    taux_flotte = models.SmallIntegerField(blank=True, null=True)
    primenette = models.FloatField(db_column='primeNette')  # Field name made lowercase.
    accessoire = models.FloatField()
    taxe = models.FloatField()
    fondgarantie = models.FloatField(db_column='fondGarantie')  # Field name made lowercase.
    cartebrune = models.FloatField(db_column='carteBrune')  # Field name made lowercase.
    primettc = models.FloatField(db_column='primeTTC')  # Field name made lowercase.
    civilite = models.ForeignKey('ParametreCivilite', models.DO_NOTHING)
    profil = models.ForeignKey('ParametreProfil', models.DO_NOTHING)
    structure = models.CharField(max_length=20)
    taux_socio = models.SmallIntegerField(blank=True, null=True)
    categorie_socio_professionnelle = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'devisflotte_devisflotte'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ParametreActivite(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=50, blank=True, null=True)
    typeactivite = models.ForeignKey('ParametreTypeactivite', models.DO_NOTHING, db_column='typeActivite_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametre_activite'


class ParametreApporteur(models.Model):
    typeapporteur = models.BooleanField(db_column='typeApporteur')  # Field name made lowercase.
    profil = models.OneToOneField('ParametreProfil', models.DO_NOTHING)
    visible = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'parametre_apporteur'


class ParametreAvenant(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    dateavenant = models.DateField(db_column='dateAvenant')  # Field name made lowercase.
    dateeffet = models.DateField(db_column='dateEffet')  # Field name made lowercase.
    dateecheance = models.DateField(db_column='dateEcheance')  # Field name made lowercase.
    primenette = models.IntegerField(db_column='primeNette')  # Field name made lowercase.
    accessoire = models.IntegerField()
    taxe = models.IntegerField()
    primettc = models.IntegerField(db_column='primeTTC')  # Field name made lowercase.
    etatavenant = models.CharField(db_column='etatAvenant', max_length=1)  # Field name made lowercase.
    numero = models.SmallIntegerField()
    ristourne = models.IntegerField()
    archive = models.BooleanField()
    valide = models.BooleanField()
    observation = models.TextField(blank=True, null=True)
    client = models.ForeignKey('ParametreClient', models.DO_NOTHING)
    contrat = models.ForeignKey('ParametreContrat', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_avenant'


class ParametreAvenantdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    objet = models.CharField(max_length=255)
    document = models.CharField(max_length=100, blank=True, null=True)
    datedepot = models.DateField(db_column='dateDepot')  # Field name made lowercase.
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_avenantdocument'


class ParametreAvenantgarantie(models.Model):
    capitaux = models.CharField(max_length=255)
    franchise = models.CharField(max_length=255)
    niveau = models.SmallIntegerField()
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)
    garantie = models.ForeignKey('ParametreGarantie', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_avenantgarantie'


class ParametreBranche(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)
    typebranche = models.ForeignKey('ParametreTypebranche', models.DO_NOTHING, db_column='typeBranche_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametre_branche'


class ParametreBrancheGaranties(models.Model):
    branche = models.ForeignKey(ParametreBranche, models.DO_NOTHING)
    garantie = models.ForeignKey('ParametreGarantie', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_branche_garanties'
        unique_together = (('branche', 'garantie'),)


class ParametreCanal(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_canal'


class ParametreCategorie(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_categorie'


class ParametreCivilite(models.Model):
    libelle = models.CharField(unique=True, max_length=50)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_civilite'


class ParametreClient(models.Model):
    typeclient = models.CharField(db_column='typeClient', max_length=1)  # Field name made lowercase.
    sexe = models.CharField(max_length=1)
    situationmatrimoniale = models.CharField(db_column='situationMatrimoniale', max_length=1)  # Field name made lowercase.
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255, blank=True, null=True)
    contactnom = models.CharField(db_column='contactNom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    situationgeographique = models.CharField(db_column='situationGeographique', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(max_length=20, blank=True, null=True)
    cellulaire = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    canal = models.ForeignKey(ParametreCanal, models.DO_NOTHING)
    civilite = models.ForeignKey(ParametreCivilite, models.DO_NOTHING)
    fonction = models.ForeignKey('ParametreFonction', models.DO_NOTHING)
    profession = models.ForeignKey('ParametreProfession', models.DO_NOTHING)
    typeactivite = models.ForeignKey('ParametreTypeactivite', models.DO_NOTHING, db_column='typeActivite_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametre_client'


class ParametreClientdocument(models.Model):
    document = models.CharField(max_length=100, blank=True, null=True)
    client = models.ForeignKey(ParametreClient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_clientdocument'


class ParametreCloture(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_cloture = models.CharField(max_length=15)
    date_cloture = models.DateField()
    etat = models.BooleanField()
    exercice = models.ForeignKey('ParametreExercice', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_cloture'
        unique_together = (('exercice', 'type_cloture'),)


class ParametreCommission(models.Model):
    typecommission = models.CharField(db_column='typeCommission', max_length=1)  # Field name made lowercase.
    taux = models.FloatField()
    dateeffet = models.DateField(db_column='dateEffet')  # Field name made lowercase.
    apporteur = models.ForeignKey(ParametreApporteur, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_commission'


class ParametreCommune(models.Model):
    libelle = models.CharField(unique=True, max_length=50)
    abrege = models.CharField(max_length=255, blank=True, null=True)
    ville = models.ForeignKey('ParametreVille', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_commune'


class ParametreCompagnie(models.Model):
    raisonsociale = models.CharField(db_column='raisonSociale', unique=True, max_length=50)  # Field name made lowercase.
    sigle = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    cellulaire = models.CharField(max_length=20, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    siege = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    visible = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'parametre_compagnie'


class ParametreContinent(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_continent'


class ParametreContrat(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    police = models.CharField(unique=True, max_length=30)
    etatcontrat = models.CharField(db_column='etatContrat', max_length=1)  # Field name made lowercase.
    datecontrat = models.DateField(db_column='dateContrat')  # Field name made lowercase.
    apporteur = models.ForeignKey(ParametreApporteur, models.DO_NOTHING)
    branche = models.ForeignKey(ParametreBranche, models.DO_NOTHING)
    compagnie = models.ForeignKey(ParametreCompagnie, models.DO_NOTHING)
    structure = models.CharField(max_length=20)
    profil = models.ForeignKey('ParametreProfil', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_contrat'


class ParametreDepartement(models.Model):
    libelle = models.CharField(unique=True, max_length=50)
    abrege = models.CharField(max_length=255, blank=True, null=True)
    region = models.ForeignKey('ParametreRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_departement'


class ParametreDepotreglementcommission(models.Model):
    id = models.BigAutoField(primary_key=True)
    montant = models.FloatField()
    mode = models.BooleanField()
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)
    paiement_reglement_commission = models.ForeignKey('ParametrePaiementreglementcommission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_depotreglementcommission'


class ParametreExercice(models.Model):
    id = models.BigAutoField(primary_key=True)
    annee = models.CharField(unique=True, max_length=15)
    date_debut = models.DateField()
    date_fin = models.DateField()
    date_cloture = models.DateField()
    etat = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'parametre_exercice'


class ParametreFonction(models.Model):
    libelle = models.CharField(unique=True, max_length=50)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_fonction'


class ParametreGarantie(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_garantie'


class ParametreGarantiebranche(models.Model):
    ordre = models.SmallIntegerField()
    branche = models.ForeignKey(ParametreBranche, models.DO_NOTHING)
    garantie = models.ForeignKey(ParametreGarantie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_garantiebranche'


class ParametrePaiementclient(models.Model):
    datepaiement = models.DateField(db_column='datePaiement')  # Field name made lowercase.
    modepaiement = models.CharField(db_column='modePaiement', max_length=1)  # Field name made lowercase.
    montant = models.IntegerField()
    observation = models.CharField(max_length=225)
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_paiementclient'


class ParametrePaiementcommission(models.Model):
    datepaiement = models.DateField(db_column='datePaiement')  # Field name made lowercase.
    modepaiement = models.CharField(db_column='modePaiement', max_length=1)  # Field name made lowercase.
    montant = models.IntegerField()
    observation = models.CharField(max_length=225)
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_paiementcommission'


class ParametrePaiementreglementcommission(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_paiement_reglement = models.CharField(max_length=15)
    date_paiement_reglement = models.DateField(blank=True, null=True)
    montant = models.FloatField()
    modepaiement = models.CharField(db_column='modePaiement', max_length=1)  # Field name made lowercase.
    reference = models.CharField(max_length=225)
    observation = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'parametre_paiementreglementcommission'


class ParametrePays(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=255, blank=True, null=True)
    continent = models.ForeignKey(ParametreContinent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_pays'


class ParametreProfession(models.Model):
    libelle = models.CharField(unique=True, max_length=50)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_profession'


class ParametreProfil(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    cellulaire = models.CharField(max_length=20, blank=True, null=True)
    sexe = models.CharField(max_length=1)
    photo = models.CharField(max_length=100, blank=True, null=True)
    fonction = models.ForeignKey(ParametreFonction, models.DO_NOTHING)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    civilite = models.ForeignKey(ParametreCivilite, models.DO_NOTHING)
    profession = models.ForeignKey(ParametreProfession, models.DO_NOTHING)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_profil'


class ParametreRegion(models.Model):
    libelle = models.CharField(unique=True, max_length=50)
    abrege = models.CharField(max_length=255, blank=True, null=True)
    pays = models.ForeignKey(ParametrePays, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_region'


class ParametreReglementcommission(models.Model):
    montant = models.IntegerField()
    datecommission = models.DateField(db_column='dateCommission', blank=True, null=True)  # Field name made lowercase.
    observation = models.CharField(max_length=225)
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)
    modepaiement = models.CharField(db_column='modePaiement', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametre_reglementcommission'


class ParametreRemboursementclient(models.Model):
    dateremboursement = models.DateField(db_column='dateRemboursement')  # Field name made lowercase.
    moderemboursement = models.CharField(db_column='modeRemboursement', max_length=1)  # Field name made lowercase.
    montant = models.IntegerField()
    observation = models.CharField(max_length=225)
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_remboursementclient'


class ParametreService(models.Model):
    libelle = models.CharField(unique=True, max_length=50)
    abrege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_service'


class ParametreSociete(models.Model):
    raisonsociale = models.CharField(db_column='raisonSociale', max_length=255)  # Field name made lowercase.
    sigle = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    cellulaire = models.CharField(max_length=20, blank=True, null=True)
    pagination = models.IntegerField()
    photo = models.CharField(max_length=100, blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    alerte_email_jour = models.IntegerField(blank=True, null=True)
    dateenvoiemail = models.DateField(db_column='dateEnvoiEmail', blank=True, null=True)  # Field name made lowercase.
    envoiemaileffectue = models.BooleanField(db_column='envoiEmailEffectue')  # Field name made lowercase.
    nbrejourmaxdateecheance = models.SmallIntegerField(db_column='nbreJourMaxDateEcheance', blank=True, null=True)  # Field name made lowercase.
    entete_table = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'parametre_societe'


class ParametreSousgarantie(models.Model):
    hierarchie = models.IntegerField()
    ordre = models.SmallIntegerField()
    retrait = models.SmallIntegerField()
    garantie = models.ForeignKey(ParametreGarantie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_sousgarantie'


class ParametreTaux(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=50, blank=True, null=True)
    taux = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_taux'


class ParametreTauxcommission(models.Model):
    taux = models.FloatField()
    branche = models.ForeignKey(ParametreBranche, models.DO_NOTHING)
    compagnie_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parametre_tauxcommission'


class ParametreTypeactivite(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_typeactivite'


class ParametreTypebranche(models.Model):
    libelle = models.CharField(unique=True, max_length=50)
    abrege = models.CharField(max_length=255, blank=True, null=True)
    renouvelable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametre_typebranche'


class ParametreVille(models.Model):
    libelle = models.CharField(unique=True, max_length=50)
    abrege = models.CharField(max_length=255, blank=True, null=True)
    departement = models.ForeignKey(ParametreDepartement, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'parametre_ville'


class ProspectionAction(models.Model):
    objet = models.CharField(max_length=255)
    dateaction = models.DateField(db_column='dateAction', blank=True, null=True)  # Field name made lowercase.
    contenu = models.TextField(blank=True, null=True)
    realisee = models.BooleanField()
    daterealisation = models.DateField(db_column='dateRealisation', blank=True, null=True)  # Field name made lowercase.
    avancement = models.ForeignKey('ProspectionAvancement', models.DO_NOTHING)
    typeaction = models.ForeignKey('ProspectionTypeaction', models.DO_NOTHING, db_column='typeAction_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prospection_action'


class ProspectionAvancement(models.Model):
    dateavancement = models.DateField(db_column='dateAvancement')  # Field name made lowercase.
    etape = models.ForeignKey('ProspectionEtape', models.DO_NOTHING)
    opportunite = models.ForeignKey('ProspectionOpportunite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prospection_avancement'


class ProspectionEtape(models.Model):
    libelle = models.CharField(unique=True, max_length=50)
    abrege = models.CharField(max_length=50, blank=True, null=True)
    probabilite = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'prospection_etape'


class ProspectionObjectif(models.Model):
    periode = models.CharField(max_length=15)
    montant = models.IntegerField()
    du = models.DateField(blank=True, null=True)
    au = models.DateField(blank=True, null=True)
    apporteur = models.OneToOneField(ParametreApporteur, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prospection_objectif'


class ProspectionOpportunite(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    datecreation = models.DateField(db_column='dateCreation', blank=True, null=True)  # Field name made lowercase.
    datemodification = models.DateField(db_column='dateModification', blank=True, null=True)  # Field name made lowercase.
    dateouverture = models.DateField(db_column='dateOuverture', blank=True, null=True)  # Field name made lowercase.
    datefermeture = models.DateField(db_column='dateFermeture', blank=True, null=True)  # Field name made lowercase.
    priorite = models.CharField(max_length=20)
    etat = models.CharField(max_length=1, blank=True, null=True)
    statut = models.CharField(max_length=1)
    montantestime = models.IntegerField(db_column='montantEstime')  # Field name made lowercase.
    prime = models.IntegerField()
    observation = models.CharField(max_length=255, blank=True, null=True)
    transforme = models.BooleanField()
    branche = models.ForeignKey(ParametreBranche, models.DO_NOTHING)
    compagnie = models.ForeignKey(ParametreCompagnie, models.DO_NOTHING)
    prospect = models.ForeignKey('ProspectionProspect', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prospection_opportunite'


class ProspectionProspect(models.Model):
    typeprospect = models.CharField(db_column='typeProspect', max_length=1)  # Field name made lowercase.
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255, blank=True, null=True)
    contactnom = models.CharField(db_column='contactNom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    situationgeographique = models.CharField(db_column='situationGeographique', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(max_length=20, blank=True, null=True)
    cellulaire = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    apporteur = models.ForeignKey(ParametreApporteur, models.DO_NOTHING)
    canal = models.ForeignKey(ParametreCanal, models.DO_NOTHING)
    civilite = models.ForeignKey(ParametreCivilite, models.DO_NOTHING)
    profession = models.ForeignKey(ParametreProfession, models.DO_NOTHING)
    typeactivite = models.ForeignKey(ParametreTypeactivite, models.DO_NOTHING, db_column='typeActivite_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prospection_prospect'


class ProspectionTache(models.Model):
    objet = models.CharField(max_length=255)
    datecreation = models.DateField(db_column='dateCreation')  # Field name made lowercase.
    datedebut = models.DateField(db_column='dateDebut')  # Field name made lowercase.
    datefin = models.DateField(db_column='dateFin')  # Field name made lowercase.
    execute = models.BooleanField()
    supprime = models.BooleanField()
    apporteur = models.ForeignKey(ParametreApporteur, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prospection_tache'


class ProspectionTypeaction(models.Model):
    libelle = models.CharField(unique=True, max_length=255)
    abrege = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prospection_typeaction'


class SanteeffectifBeneficiairecollege(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=300, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    primenette = models.IntegerField(db_column='primeNette')  # Field name made lowercase.
    statut = models.CharField(max_length=20)
    datenaissance = models.DateField(db_column='dateNaissance', blank=True, null=True)  # Field name made lowercase.
    dateentree = models.DateField(db_column='dateEntree', blank=True, null=True)  # Field name made lowercase.
    dateretrait = models.DateField(db_column='dateRetrait', blank=True, null=True)  # Field name made lowercase.
    retrait = models.BooleanField()
    incorpore = models.BooleanField()
    civilite = models.ForeignKey(ParametreCivilite, models.DO_NOTHING)
    famille = models.ForeignKey('SanteeffectifFamille', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'santeeffectif_beneficiairecollege'


class SanteeffectifBeneficiairetampon(models.Model):
    codecollege = models.IntegerField(db_column='codeCollege')  # Field name made lowercase.
    numerofamille = models.CharField(db_column='numeroFamille', max_length=255)  # Field name made lowercase.
    numero = models.CharField(max_length=255)
    nom = models.CharField(max_length=255, blank=True, null=True)
    prenoms = models.CharField(max_length=300, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    primenette = models.IntegerField(db_column='primeNette')  # Field name made lowercase.
    statut = models.CharField(max_length=20)
    datenaissance = models.DateField(db_column='dateNaissance', blank=True, null=True)  # Field name made lowercase.
    dateentree = models.DateField(db_column='dateEntree', blank=True, null=True)  # Field name made lowercase.
    compagnie = models.CharField(max_length=255, blank=True, null=True)
    incorpore = models.BooleanField()
    civilite = models.ForeignKey(ParametreCivilite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'santeeffectif_beneficiairetampon'


class SanteeffectifCollege(models.Model):
    libelle = models.CharField(max_length=255, blank=True, null=True)
    primenette = models.IntegerField(db_column='primeNette')  # Field name made lowercase.
    taux = models.CharField(max_length=255, blank=True, null=True)
    effectiffamille = models.IntegerField(db_column='effectifFamille')  # Field name made lowercase.
    dateentree = models.DateField(db_column='dateEntree', blank=True, null=True)  # Field name made lowercase.
    dateretrait = models.DateField(db_column='dateRetrait', blank=True, null=True)  # Field name made lowercase.
    retrait = models.BooleanField()
    incorpore = models.BooleanField()
    contrat = models.ForeignKey(ParametreContrat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'santeeffectif_college'


class SanteeffectifCollegegarantie(models.Model):
    tauxremboursement = models.CharField(db_column='tauxRemboursement', max_length=255, blank=True, null=True)  # Field name made lowercase.
    plafondremboursement = models.CharField(db_column='plafondRemboursement', max_length=255, blank=True, null=True)  # Field name made lowercase.
    niveau = models.SmallIntegerField(blank=True, null=True)
    college = models.ForeignKey(SanteeffectifCollege, models.DO_NOTHING)
    garantie = models.ForeignKey(ParametreGarantie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'santeeffectif_collegegarantie'


class SanteeffectifDetailstransaction(models.Model):
    periodedu = models.DateField(db_column='periodeDu')  # Field name made lowercase.
    periodeau = models.DateField(db_column='periodeAu')  # Field name made lowercase.
    typetransaction = models.CharField(db_column='typeTransaction', max_length=20)  # Field name made lowercase.
    primenette = models.IntegerField(db_column='primeNette')  # Field name made lowercase.
    observation = models.CharField(max_length=255)
    transaction = models.ForeignKey('SanteeffectifTransaction', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'santeeffectif_detailstransaction'


class SanteeffectifFamille(models.Model):
    statut = models.CharField(max_length=20)
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    effectifbeneficiaire = models.SmallIntegerField(db_column='effectifBeneficiaire', blank=True, null=True)  # Field name made lowercase.
    datenaissance = models.DateField(db_column='dateNaissance', blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(max_length=1)
    primenette = models.IntegerField(db_column='primeNette')  # Field name made lowercase.
    dateentree = models.DateField(db_column='dateEntree')  # Field name made lowercase.
    dateretrait = models.DateField(db_column='dateRetrait')  # Field name made lowercase.
    retrait = models.BooleanField()
    incorpore = models.BooleanField()
    civilite = models.ForeignKey(ParametreCivilite, models.DO_NOTHING)
    college = models.ForeignKey(SanteeffectifCollege, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'santeeffectif_famille'


class SanteeffectifSantetransaction(models.Model):
    quoi = models.CharField(max_length=255)
    qui = models.CharField(max_length=255)
    quand = models.DateField()
    datetransaction = models.DateField(db_column='dateTransaction')  # Field name made lowercase.
    observation = models.CharField(max_length=255)
    contrat = models.ForeignKey(ParametreContrat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'santeeffectif_santetransaction'


class SanteeffectifTampon(models.Model):
    numerofamille = models.CharField(db_column='numeroFamille', max_length=255)  # Field name made lowercase.
    numero = models.CharField(max_length=255)
    nom = models.CharField(max_length=255, blank=True, null=True)
    prenoms = models.CharField(max_length=300, blank=True, null=True)
    statut = models.CharField(max_length=20)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    datenaissance = models.DateField(db_column='dateNaissance', blank=True, null=True)  # Field name made lowercase.
    dateentree = models.DateField(db_column='dateEntree', blank=True, null=True)  # Field name made lowercase.
    client = models.CharField(max_length=255, blank=True, null=True)
    libelle = models.CharField(max_length=255, blank=True, null=True)
    taux = models.CharField(max_length=255, blank=True, null=True)
    incorpore = models.BooleanField()
    civilite = models.ForeignKey(ParametreCivilite, models.DO_NOTHING)
    transfere = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'santeeffectif_tampon'


class SanteeffectifTransaction(models.Model):
    datetransaction = models.DateField(db_column='dateTransaction')  # Field name made lowercase.
    accessoire = models.IntegerField()
    taxe = models.IntegerField()
    observation = models.CharField(max_length=255)
    contrat = models.ForeignKey(ParametreContrat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'santeeffectif_transaction'


class SanteindividuelleAvenantgarantiesante(models.Model):
    tauxremboursement = models.CharField(db_column='tauxRemboursement', max_length=255)  # Field name made lowercase.
    plafondremboursement = models.CharField(db_column='plafondRemboursement', max_length=255)  # Field name made lowercase.
    niveau = models.SmallIntegerField()
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)
    garantie = models.ForeignKey(ParametreGarantie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'santeindividuelle_avenantgarantiesante'


class SanteindividuelleBeneficiaire(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=300, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    statut = models.CharField(max_length=20)
    datenaissance = models.DateField(db_column='dateNaissance', blank=True, null=True)  # Field name made lowercase.
    dateentree = models.DateField(db_column='dateEntree', blank=True, null=True)  # Field name made lowercase.
    dateretrait = models.DateField(db_column='dateRetrait', blank=True, null=True)  # Field name made lowercase.
    retrait = models.BooleanField()
    primenette = models.IntegerField(db_column='primeNette')  # Field name made lowercase.
    incorpore = models.BooleanField()
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)
    civilite = models.ForeignKey(ParametreCivilite, models.DO_NOTHING)
    id_parent_retire = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'santeindividuelle_beneficiaire'


class SanteindividuelleBeneficiaireretire(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=300, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    statut = models.CharField(max_length=20)
    datenaissance = models.DateField(db_column='dateNaissance', blank=True, null=True)  # Field name made lowercase.
    dateentree = models.DateField(db_column='dateEntree', blank=True, null=True)  # Field name made lowercase.
    dateretrait = models.DateField(db_column='dateRetrait', blank=True, null=True)  # Field name made lowercase.
    retrait = models.BooleanField()
    primenette = models.IntegerField(db_column='primeNette')  # Field name made lowercase.
    incorpore = models.BooleanField()
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)
    civilite = models.ForeignKey(ParametreCivilite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'santeindividuelle_beneficiaireretire'


class SinistreActionsinistre(models.Model):
    libelle = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sinistre_actionsinistre'


class SinistreEtapeaction(models.Model):
    numero = models.SmallIntegerField()
    actionsinistre = models.ForeignKey(SinistreActionsinistre, models.DO_NOTHING, db_column='actionSinistre_id')  # Field name made lowercase.
    etapesinistre = models.ForeignKey('SinistreEtapesinistre', models.DO_NOTHING, db_column='etapeSinistre_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sinistre_etapeaction'


class SinistreEtapesinistre(models.Model):
    libelle = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sinistre_etapesinistre'


class SinistreEtapesinistreBranches(models.Model):
    etapesinistre = models.ForeignKey(SinistreEtapesinistre, models.DO_NOTHING)
    branche = models.ForeignKey(ParametreBranche, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sinistre_etapesinistre_branches'
        unique_together = (('etapesinistre', 'branche'),)


class SinistreRemboursement(models.Model):
    objet = models.CharField(max_length=255)
    dateremboursement = models.DateField(db_column='dateRemboursement')  # Field name made lowercase.
    montant = models.IntegerField()
    sinistre = models.ForeignKey('SinistreSinistre', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sinistre_remboursement'


class SinistreRemboursementdossier(models.Model):
    datedossier = models.DateField(db_column='dateDossier')  # Field name made lowercase.
    dossier = models.TextField()
    image = models.CharField(max_length=100)
    document = models.CharField(max_length=100)
    remboursement = models.ForeignKey(SinistreRemboursement, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sinistre_remboursementdossier'


class SinistreSinistre(models.Model):
    typedeclaration = models.CharField(db_column='typeDeclaration', max_length=50)  # Field name made lowercase.
    objet = models.TextField(blank=True, null=True)
    datesinistre = models.DateField(db_column='dateSinistre')  # Field name made lowercase.
    datedeclaration = models.DateField(db_column='dateDeclaration')  # Field name made lowercase.
    dossier = models.CharField(max_length=255)
    dossierinterne = models.CharField(db_column='dossierInterne', max_length=255, blank=True, null=True)  # Field name made lowercase.
    observation = models.CharField(max_length=255, blank=True, null=True)
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)
    etatdossier = models.CharField(db_column='etatDossier', max_length=50)  # Field name made lowercase.
    valide = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sinistre_sinistre'


class SinistreSinistreclient(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_transaction = models.CharField(max_length=50)
    police = models.CharField(max_length=255)
    date_transaction = models.DateField()
    observation = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sinistre_sinistreclient'


class SinistreSinistreclientdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    objet = models.CharField(max_length=255)
    document = models.CharField(max_length=100)
    sinistreclient = models.ForeignKey(SinistreSinistreclient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sinistre_sinistreclientdocument'


class SinistreSinistredocument(models.Model):
    objet = models.CharField(max_length=255)
    document = models.CharField(max_length=100)
    datedepot = models.DateField(db_column='dateDepot')  # Field name made lowercase.
    sinistre = models.ForeignKey(SinistreSinistre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sinistre_sinistredocument'


class SinistreSinistreetape(models.Model):
    valide = models.BooleanField()
    etapesinistre = models.ForeignKey(SinistreEtapesinistre, models.DO_NOTHING, db_column='etapeSinistre_id')  # Field name made lowercase.
    sinistre = models.ForeignKey(SinistreSinistre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sinistre_sinistreetape'


class SinistreSinistreetapeaction(models.Model):
    intervenant = models.CharField(max_length=255, blank=True, null=True)
    moment = models.CharField(max_length=255, blank=True, null=True)
    valide = models.BooleanField()
    etapeaction = models.ForeignKey(SinistreEtapeaction, models.DO_NOTHING, db_column='etapeAction_id')  # Field name made lowercase.
    sinistre = models.ForeignKey(SinistreSinistre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sinistre_sinistreetapeaction'


class SinistreSinistrerisquedivers(models.Model):
    typedeclaration = models.CharField(db_column='typeDeclaration', max_length=50)  # Field name made lowercase.
    typesinistre = models.CharField(db_column='typeSinistre', max_length=50)  # Field name made lowercase.
    objet = models.TextField(blank=True, null=True)
    datesinistre = models.DateField(db_column='dateSinistre')  # Field name made lowercase.
    datedeclaration = models.DateField(db_column='dateDeclaration')  # Field name made lowercase.
    dossier = models.CharField(max_length=255)
    dossierinterne = models.CharField(db_column='dossierInterne', max_length=255)  # Field name made lowercase.
    transmis = models.BooleanField()
    observation = models.CharField(max_length=255, blank=True, null=True)
    circonstance = models.TextField(blank=True, null=True)
    degat = models.TextField(blank=True, null=True)
    lieu = models.CharField(max_length=255, blank=True, null=True)
    constat = models.BooleanField()
    datetransmission = models.DateField(db_column='dateTransmission', blank=True, null=True)  # Field name made lowercase.
    etatdossier = models.CharField(db_column='etatDossier', max_length=50)  # Field name made lowercase.
    evaluationprejudice = models.IntegerField(db_column='evaluationPrejudice')  # Field name made lowercase.
    infoconstat = models.CharField(db_column='infoConstat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bonreparation = models.BooleanField(db_column='bonReparation')  # Field name made lowercase.
    datebonreparation = models.DateField(db_column='dateBonReparation', blank=True, null=True)  # Field name made lowercase.
    bonsortie = models.BooleanField(db_column='bonSortie')  # Field name made lowercase.
    datebonsortie = models.DateField(db_column='dateBonSortie', blank=True, null=True)  # Field name made lowercase.
    bonremplacement = models.BooleanField(db_column='bonRemplacement')  # Field name made lowercase.
    datebonremplacement = models.DateField(db_column='dateBonRemplacement', blank=True, null=True)  # Field name made lowercase.
    montant = models.IntegerField()
    avenant = models.ForeignKey(ParametreAvenant, models.DO_NOTHING)
    immatriculation = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'sinistre_sinistrerisquedivers'


class SinistreSinistresante(models.Model):
    categorie = models.CharField(max_length=50)
    prestation = models.CharField(max_length=50)
    validation = models.CharField(max_length=50)
    beneficiaire = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    assure = models.CharField(max_length=255)
    numeroassure = models.CharField(db_column='numeroAssure', max_length=255)  # Field name made lowercase.
    montant = models.IntegerField()
    dateenvoi = models.DateField(db_column='dateEnvoi', blank=True, null=True)  # Field name made lowercase.
    datereception = models.DateField(db_column='dateReception', blank=True, null=True)  # Field name made lowercase.
    dateremise = models.DateField(db_column='dateRemise', blank=True, null=True)  # Field name made lowercase.
    sinistre = models.ForeignKey(SinistreSinistre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sinistre_sinistresante'


class SinistreSinistresantedocument(models.Model):
    document = models.CharField(max_length=100)
    datedepot = models.DateField(db_column='dateDepot')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sinistre_sinistresantedocument'


class SinistreSinistresuiviauto(models.Model):
    carte_grise = models.BooleanField()
    permis_conduire = models.BooleanField()
    photo_vehicule = models.BooleanField()
    visite_technique = models.BooleanField()
    cinquieme_etape = models.BooleanField()
    deuxieme_etape = models.BooleanField()
    duree_cinquieme_etape = models.SmallIntegerField()
    duree_deuxieme_etape = models.SmallIntegerField()
    duree_premiere_etape = models.SmallIntegerField()
    duree_quatrieme_etape = models.SmallIntegerField()
    duree_septieme_etape = models.SmallIntegerField()
    duree_sixieme_etape = models.SmallIntegerField()
    duree_troisieme_etape = models.SmallIntegerField()
    premiere_etape = models.BooleanField()
    quatrieme_etape = models.BooleanField()
    septieme_etape = models.BooleanField()
    sixieme_etape = models.BooleanField()
    troisieme_etape = models.BooleanField()
    date_etablissement_cheque = models.DateField()
    date_transmission_cheque = models.DateField()
    etablissement_cheque = models.BooleanField()
    sinistre = models.ForeignKey(SinistreSinistre, models.DO_NOTHING)
    transmission_cheque = models.BooleanField()
    typesinistre = models.CharField(db_column='typeSinistre', max_length=100)  # Field name made lowercase.
    circonstance = models.TextField(blank=True, null=True)
    constat = models.BooleanField()
    dateconstat = models.DateField(db_column='dateConstat')  # Field name made lowercase.
    datetransmission = models.DateField(db_column='dateTransmission', blank=True, null=True)  # Field name made lowercase.
    degat = models.TextField(blank=True, null=True)
    evaluationprejudice = models.IntegerField(db_column='evaluationPrejudice')  # Field name made lowercase.
    infoconstat = models.CharField(db_column='infoConstat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lieu = models.CharField(max_length=255, blank=True, null=True)
    observation = models.CharField(max_length=255, blank=True, null=True)
    transmis = models.BooleanField()
    attestation_vol = models.BooleanField()
    bonremplacement = models.BooleanField(db_column='bonRemplacement')  # Field name made lowercase.
    bonreparation = models.BooleanField(db_column='bonReparation')  # Field name made lowercase.
    bonsortie = models.BooleanField(db_column='bonSortie')  # Field name made lowercase.
    chequenumero = models.CharField(db_column='chequeNumero', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateattestationvol = models.DateField(db_column='dateAttestationVol')  # Field name made lowercase.
    datebonremplacement = models.DateField(db_column='dateBonRemplacement')  # Field name made lowercase.
    datebonreparation = models.DateField(db_column='dateBonReparation')  # Field name made lowercase.
    datebonsortie = models.DateField(db_column='dateBonSortie')  # Field name made lowercase.
    dateexpert = models.DateField(db_column='dateExpert')  # Field name made lowercase.
    datefacturereparation = models.DateField(db_column='dateFactureReparation')  # Field name made lowercase.
    expert = models.BooleanField()
    facturereparation = models.BooleanField(db_column='factureReparation')  # Field name made lowercase.
    infoexpert = models.CharField(db_column='infoExpert', max_length=255, blank=True, null=True)  # Field name made lowercase.
    montant = models.IntegerField()
    situationrisque = models.CharField(db_column='situationRisque', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valide = models.BooleanField()
    vehicule_id = models.IntegerField()
    certificatconsolidation = models.BooleanField(db_column='certificatConsolidation')  # Field name made lowercase.
    datecertificatconsolidation = models.DateField(db_column='dateCertificatConsolidation')  # Field name made lowercase.
    datefacturenormalisee = models.DateField(db_column='dateFactureNormalisee')  # Field name made lowercase.
    datepiecesoins = models.DateField(db_column='datePieceSoins')  # Field name made lowercase.
    daterapportmedical = models.DateField(db_column='dateRapportMedical')  # Field name made lowercase.
    facturenormalisee = models.BooleanField(db_column='factureNormalisee')  # Field name made lowercase.
    piecesoins = models.BooleanField(db_column='pieceSoins')  # Field name made lowercase.
    rapportmedical = models.BooleanField(db_column='rapportMedical')  # Field name made lowercase.
    certificatdepensemort = models.BooleanField(db_column='certificatDepenseMort')  # Field name made lowercase.
    cniayantdroitmajeur = models.BooleanField(db_column='cniAyantDroitMajeur')  # Field name made lowercase.
    cniayantdroitmineur = models.BooleanField(db_column='cniAyantDroitMineur')  # Field name made lowercase.
    datecertificatdepensemort = models.DateField(db_column='dateCertificatDepenseMort')  # Field name made lowercase.
    datecniayantdroitmajeur = models.DateField(db_column='dateCniAyantDroitMajeur')  # Field name made lowercase.
    datecniayantdroitmineur = models.DateField(db_column='dateCniAyantDroitMineur')  # Field name made lowercase.
    dateextraitactedeces = models.DateField(db_column='dateExtraitActeDeces')  # Field name made lowercase.
    datepuissancepartenelle = models.DateField(db_column='datePuissancePartenelle')  # Field name made lowercase.
    extraitactedeces = models.BooleanField(db_column='extraitActeDeces')  # Field name made lowercase.
    puissancepartenelle = models.BooleanField(db_column='puissancePartenelle')  # Field name made lowercase.
    element_dossier = models.CharField(max_length=500, blank=True, null=True)
    garage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinistre_sinistresuiviauto'


class SinistreSinistresuivirisquesdivers(models.Model):
    typesinistre = models.CharField(db_column='typeSinistre', max_length=100)  # Field name made lowercase.
    element_dossier = models.CharField(max_length=255, blank=True, null=True)
    premiere_etape = models.BooleanField()
    duree_premiere_etape = models.SmallIntegerField()
    deuxieme_etape = models.BooleanField()
    duree_deuxieme_etape = models.SmallIntegerField()
    troisieme_etape = models.BooleanField()
    duree_troisieme_etape = models.SmallIntegerField()
    quatrieme_etape = models.BooleanField()
    duree_quatrieme_etape = models.SmallIntegerField()
    cinquieme_etape = models.BooleanField()
    duree_cinquieme_etape = models.SmallIntegerField()
    sixieme_etape = models.BooleanField()
    duree_sixieme_etape = models.SmallIntegerField()
    septieme_etape = models.BooleanField()
    duree_septieme_etape = models.SmallIntegerField()
    transmis = models.BooleanField()
    observation = models.CharField(max_length=255, blank=True, null=True)
    circonstance = models.TextField(blank=True, null=True)
    degat = models.TextField(blank=True, null=True)
    lieu = models.CharField(max_length=255, blank=True, null=True)
    datetransmission = models.DateField(db_column='dateTransmission', blank=True, null=True)  # Field name made lowercase.
    evaluationprejudice = models.IntegerField(db_column='evaluationPrejudice')  # Field name made lowercase.
    missionexpertise = models.BooleanField(db_column='missionExpertise')  # Field name made lowercase.
    infoexpert = models.CharField(db_column='infoExpert', max_length=255, blank=True, null=True)  # Field name made lowercase.
    infomission = models.TextField(db_column='infoMission', blank=True, null=True)  # Field name made lowercase.
    datemission = models.DateField(db_column='dateMission')  # Field name made lowercase.
    transmissionrapportexpertiseclient = models.BooleanField(db_column='transmissionRapportExpertiseClient')  # Field name made lowercase.
    datetransmissionrapportexpertiseclient = models.DateField(db_column='datetransmissionRapportExpertiseClient', blank=True, null=True)  # Field name made lowercase.
    rapport_expertise = models.CharField(max_length=255, blank=True, null=True)
    etablissement_cheque = models.BooleanField()
    date_etablissement_cheque = models.DateField()
    transmission_cheque = models.BooleanField()
    date_transmission_cheque = models.DateField()
    montant = models.IntegerField()
    valide = models.BooleanField()
    chequenumero = models.CharField(db_column='chequeNumero', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sinistre = models.ForeignKey(SinistreSinistre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sinistre_sinistresuivirisquesdivers'


class SinistreSinistresuivisante(models.Model):
    centre_hospitalier = models.CharField(max_length=50)
    categorie = models.CharField(max_length=50)
    prestation = models.CharField(max_length=50)
    consultation = models.CharField(max_length=255, blank=True, null=True)
    hospitalisation = models.CharField(max_length=255, blank=True, null=True)
    accouchement_public = models.CharField(max_length=255, blank=True, null=True)
    accouchement_prive = models.CharField(max_length=255, blank=True, null=True)
    pharmacie = models.CharField(max_length=255, blank=True, null=True)
    premiere_etape = models.BooleanField()
    duree_premiere_etape = models.SmallIntegerField()
    deuxieme_etape = models.BooleanField()
    duree_deuxieme_etape = models.SmallIntegerField()
    troisieme_etape = models.BooleanField()
    duree_troisieme_etape = models.SmallIntegerField()
    quatrieme_etape = models.BooleanField()
    duree_quatrieme_etape = models.SmallIntegerField()
    cinquieme_etape = models.BooleanField()
    duree_cinquieme_etape = models.SmallIntegerField()
    sixieme_etape = models.BooleanField()
    duree_sixieme_etape = models.SmallIntegerField()
    septieme_etape = models.BooleanField()
    duree_septieme_etape = models.SmallIntegerField()
    etablissement_cheque = models.BooleanField()
    date_etablissement_cheque = models.DateField()
    transmission_cheque = models.BooleanField()
    date_transmission_cheque = models.DateField()
    objet = models.TextField(blank=True, null=True)
    transmis = models.BooleanField()
    observation = models.CharField(max_length=255, blank=True, null=True)
    datetransmission = models.DateField(db_column='dateTransmission', blank=True, null=True)  # Field name made lowercase.
    evaluationprejudice = models.IntegerField(db_column='evaluationPrejudice')  # Field name made lowercase.
    constat = models.BooleanField()
    infoconstat = models.CharField(db_column='infoConstat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    montant = models.IntegerField()
    infoexpert = models.CharField(db_column='infoExpert', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valide = models.BooleanField()
    reception = models.BooleanField()
    datereception = models.DateField(db_column='dateReception', blank=True, null=True)  # Field name made lowercase.
    rembourse = models.BooleanField()
    dateremise = models.DateField(db_column='dateRemise', blank=True, null=True)  # Field name made lowercase.
    chequeremboursement = models.CharField(db_column='chequeRemboursement', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chequephoto = models.CharField(db_column='chequePhoto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chequenumero = models.CharField(db_column='chequeNumero', max_length=255, blank=True, null=True)  # Field name made lowercase.
    beneficiaire = models.ForeignKey(SanteeffectifBeneficiairecollege, models.DO_NOTHING)
    sinistre_id = models.IntegerField()
    element_dossier = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinistre_sinistresuivisante'
