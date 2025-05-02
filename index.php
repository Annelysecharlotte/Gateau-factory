<?php
// Traitement de la connexion
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['action']) && $_POST['action'] === 'login') {
    $email = $_POST['email'];
    $password = $_POST['password'];
    
    // TODO: Vérification en base de données
    echo "<p>Connexion demandée pour : $email</p>";
}

// Traitement de l'inscription
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['action']) && $_POST['action'] === 'signup') {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $role = $_POST['role'];

    // TODO: Enregistrement en base de données
    echo "<p>Inscription réussie pour : $username ($role)</p>";
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>CakeMaster - Connexion & Inscription</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
    <h1 class="logo">🍰 CakeMaster</h1>

    <div class="forms">
    <!-- Formulaire de connexion -->
    <div class="form login">
        <h2>Connexion</h2>
        <form method="POST">
        <input type="hidden" name="action" value="login">
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Mot de passe" required>
        <button type="submit">Se connecter</button>
        </form>
    </div>

    <!-- Formulaire d'inscription -->
    <div class="form signup">
        <h2>Inscription</h2>
        <form method="POST">
        <input type="hidden" name="action" value="signup">
        <input type="text" name="username" placeholder="Nom d'utilisateur" required>
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Mot de passe" required>
        <select name="role" required>
            <option value="">Choisir un rôle</option>
            <option value="utilisateur">Utilisateur</option>
            <option value="patissier">Pâtissier</option>
        </select>
        <button type="submit">S'inscrire</button>
        </form>
    </div>
    </div>
</div>
</body>
</html>
