const http = require('http');
const { spawn } = require('child_process');

const CRON_DIR = '/Users/piotrmatejuk/Documents/claude-cron';

const req = http.get('http://localhost:7777/api/status', { timeout: 1000 }, () => {
  process.exit(0);
});

req.on('error', () => {
  const child = spawn('node', ['server.js'], {
    cwd: CRON_DIR,
    detached: true,
    stdio: 'ignore',
  });
  child.unref();

  // Caffeinate — keep Mac awake while claude-cron is alive
  if (process.platform === 'darwin') {
    spawn('caffeinate', ['-w', String(child.pid)], {
      detached: true,
      stdio: 'ignore',
    }).unref();
  }

  console.log('🕹️ Claude-Cron started in background (localhost:7777)');
  process.exit(0);
});

req.on('timeout', () => {
  req.destroy();
});
