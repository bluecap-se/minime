import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { HashProvider } from './Contexts.js'
import Shrink from './components/layouts/Shrink'
import Result from './components/layouts/Result'
import './App.css'

function App() {
  const basename = process.env.PUBLIC_URL

  return (
    <HashProvider>
      <Router basename={basename}>
        <Routes>
          <Route path="/" exact element={<Shrink />} />
          <Route path="/result/" element={<Result />} />
        </Routes>
      </Router>
    </HashProvider>
  )
}

export default App