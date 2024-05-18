import express from 'express';
import proxy from 'express-http-proxy';

const app = express();
const PORT = process.env.PORT || 8080;

app.use('/api/orders', proxy('http://localhost:5002'));
app.use('/api/products', proxy('http://localhost:5001'));

app.listen(PORT, () => {
  console.log(`API Gateway running on http://localhost:${PORT}`);
});
