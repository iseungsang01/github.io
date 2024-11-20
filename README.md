<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles.css"> <!-- Linking external stylesheet -->
  <title>Seung Sang LEE</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    header, section {
      padding: 20px;
      text-align: center;
    }
    header {
      background-color: #f4f4f4;
    }
    main {
      margin: 0 auto;
      max-width: 800px;
    }
    button {
      margin: 5px;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      border: 1px solid #ddd;
      border-radius: 5px;
      background-color: #007BFF;
      color: white;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <!-- Header Section -->
  <header>
    <h1>Seung Sang LEE</h1>
    <p>Bachelor Student of Nuclear System Engineering and Rural Systems Engineering</p>
    <button onclick="scrollToSection('about')">About</button>
    <button onclick="scrollToSection('education-career')">Education & Career</button>
    <button onclick="scrollToSection('interests-goals')">Interests & Goals</button>
    <button onclick="scrollToSection('contact')">Contact</button>
    <button onclick="window.open('https://www.linkedin.com/in/%EC%8A%B9%EC%83%81-%EC%9D%B4-55560a27a/', '_blank')">LinkedIn</button>
  </header>

  <!-- Main Section -->
  <main>
    <!-- About Section -->
    <section id="about">
      <h2>About</h2>
      <p>Hello! I am majoring in Nuclear Engineering and Rural Systems Engineering, with a deep interest in Computer Science and Mathematics. I am acquiring knowledge at a graduate level to develop expertise in these fields, with a particular focus on algorithms, data science, and programming.</p>
    </section>

    <!-- Education and Career Section -->
    <section id="education-career">
      <h2>Education and Career</h2>
      <p>I am currently double-majoring in Nuclear Engineering and Rural Systems Engineering, aiming to promote sustainable resource management and technological development through the integration of both fields. I am particularly focused on researching the fusion of information technology and transportation technology to contribute to the efficient management of urban resources and the development of rural areas.</p>
    </section>

    <!-- Interests and Goals Section -->
    <section id="interests-goals">
      <h2>Interests and Goals</h2>
      <p>I have a deep interest in computer science algorithms, data science, and programming, and I excel in physics and computer science. I am continually growing through the exploration of various information in these fields.</p>
    </section>

    <!-- Contact Section -->
    <section id="contact">
      <h2>Contact</h2>
      <p>Email: <a href="mailto:lss010330@snu.ac.kr">lss010330@snu.ac.kr</a></p>
      <p>LinkedIn: <a href="https://www.linkedin.com/in/%EC%8A%B9%EC%83%81-%EC%9D%B4-55560a27a/" target="_blank">Visit my LinkedIn</a></p>
    </section>
  </main>

  <!-- JavaScript for Navigation -->
  <script>
    function scrollToSection(sectionId) {
      document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
    }
  </script>
</body>
</html>
