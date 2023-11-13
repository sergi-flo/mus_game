import { Route, Link, Switch } from 'wouter'
import RegistrationPage from './components/RegistrationPage'
import LoginPage from './components/LoginPage'
import './App.css'

const HomePage = () => {
  return (
    <div>
      <h1>Home Page</h1>
    </div>
  )
}

function App () {
  return (
    <div className="App">
      <header>
        <h1><Link to="/">MUS Game</Link></h1>
        <nav>
          <ul>
            <li><Link to="/register">Register</Link></li>
            <li><Link to="/login">Login</Link></li>
          </ul>
        </nav>
      </header>

      <Switch>
        <Route path="/register" component={RegistrationPage} />
        <Route path="/login" component={LoginPage} />
        <Route path="/"> <HomePage/> </Route>
        <Route path="/:rest*">{(params) => `404, Sorry the page ${params.rest} does not exist!`}</Route>
      </Switch>
    </div>
  )
}

export default App
