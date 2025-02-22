<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-Time System Resource Monitor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1e1e2e;
            color: #ffffff;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #282a36;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
        }
        h1 {
            color: #00d4ff;
            text-align: center;
        }
        h2 {
            color: #ff79c6;
        }
        code {
            background-color: #44475a;
            padding: 5px;
            border-radius: 5px;
            color: #50fa7b;
        }
        .highlight {
            color: #f1fa8c;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #bd93f9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Real-Time System Resource Monitor</h1>
        <h2>Project Description</h2>
        <p>The <span class="highlight">Real-Time System Resource Monitor</span> is a Python-based tool that provides live updates on CPU and memory usage using a simple terminal interface.</p>
        
        <h2>Key Features</h2>
        <ul>
            <li><span class="highlight">Real-time Monitoring:</span> Displays live CPU and memory usage.</li>
            <li><span class="highlight">Graphical Representation:</span> Uses progress bars to represent system load.</li>
            <li><span class="highlight">Lightweight & Efficient:</span> Runs with minimal system impact.</li>
            <li><span class="highlight">Continuous Updates:</span> Refreshes data every 0.5 seconds.</li>
        </ul>
        
        <h2>Technologies Used</h2>
        <ul>
            <li>Python</li>
            <li><code>psutil</code> library (for system metrics)</li>
            <li><code>time</code> module (for periodic updates)</li>
        </ul>
        
        <h2>Usage</h2>
        <p>Run the following command to start monitoring:</p>
        <pre><code>python monitor.py</code></pre>
        
        <div class="footer">Created with ❤️ by Dilshad Ali</div>
    </div>
</body>
</html>
