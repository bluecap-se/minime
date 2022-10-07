/* eslint-disable jsx-a11y/no-autofocus */
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useHashDispatch } from '../../Contexts.js'

const Shrink = () => {
  const [urlInput, setUrlInput] = useState('')
  const [passwordChecked, setPasswordChecked] = useState(false)
  const [passwordInput, setPasswordInput] = useState('')
  const apiDomain = process.env.REACT_APP_DOMAIN
  const navigate = useNavigate()
  const dispatch = useHashDispatch()

  const submitForm = (e) => {
    e.preventDefault()
    const data = { url: urlInput, password: passwordInput }

    const sendForm = async () => {
      try {
        const res = await fetch(`${apiDomain}/shorten/`, {
          method: 'POST',
          headers: {
            'Content-type': 'application/json',
          },
          body: JSON.stringify(data),
        })
        const output = await res.json()
        if (!output.hash) {
          throw Error()
        }

        dispatch({ hash: output.hash })
        navigate('/result/', { replace: true })
      } catch (err) {
        // TODO: Show error message to user
        console.error(err)
      }
    }
    sendForm()
  }

  return (
    <form className="form-shorten" onSubmit={submitForm}>
      <header className="text-center mb-4">
        <img
          className="mb-4 logo"
          src="/images/logo.png"
          alt="Minime logo"
          width="90"
          height="90"
        />
        <h1 className="h3 mb-3 font-weight-normal">MiniMe</h1>
        <p>Shrinking that link of yours</p>
      </header>

      <article className="panel url-form">
        <div className="form-label-group">
          <input
            type="url"
            name="url"
            placeholder="URL to shorten"
            className="form-control"
            maxLength="256"
            value={urlInput}
            onChange={(e) => setUrlInput(e.target.value.trim())}
            autoFocus
            required
          />
        </div>

        <div className="checkbox mb-3">
          <label htmlFor="usePassword">
            <input
              type="checkbox"
              id="usePassword"
              value={passwordChecked}
              onChange={() => setPasswordChecked(!passwordChecked)}
            />{' '}
            I want to gather stats
          </label>
        </div>

        {passwordChecked && (
          <div id="formPasswordField" className="form-label-group password-field">
            <input
              type="password"
              name="password"
              placeholder="Set a password"
              className="form-control"
              value={passwordInput}
              onChange={(e) => setPasswordInput(e.target.value)}
            />
          </div>
        )}

        <div className="d-grid">
          <input type="submit" className="btn btn-lg btn-primary" value="Shrink" />
        </div>
      </article>

      <footer>
        <p className="mt-3 mb-2 text-muted text-center">
          Made by{' '}
          <a href="https://bluecap.se" target="_blank" rel="noreferrer">
            Bluecap
          </a>
        </p>
      </footer>
    </form>
  )
}

export default Shrink
