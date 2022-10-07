import { useState } from 'react'
import Clipboard from 'react-clipboard.js'

const Shrink = () => {
  const [urlInput, setUrlInput] = useState('')
  const [passwordChecked, setPasswordChecked] = useState(false)
  const [passwordInput, setPasswordInput] = useState('')
  const [visibleResult, setVisibleResult] = useState(false)
  const apiDomain = process.env.REACT_APP_API_DOMAIN

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

        setUrlInput('')
        setPasswordChecked(false)
        setPasswordInput('')
        setVisibleResult(true)
      } catch (err) {
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
            // eslint-disable-next-line jsx-a11y/no-autofocus
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

      {visibleResult && (
        <article className="panel result">
          <p className="text-center" style={{ paddingTop: '10px' }}>
            <img src="/images/done-icon.png" width="60" alt="" />
          </p>
          <p className="text-center">
            <b>
              Here is your new URL:
              <br />
              <a href="/" id="hash">
                abc
              </a>
            </b>
            <Clipboard
              data-clipboard-text="<URL>"
              button-title="Copy URL to clipboard"
              className="clipboard"
            >
              <svg
                viewBox="0 0 24 24"
                width="20"
                height="20"
                stroke="currentColor"
                strokeWidth="2"
                fill="none"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2" />
                <rect x="8" y="2" width="8" height="4" rx="1" ry="1" />
              </svg>
            </Clipboard>
            <i id="copyUrl" className="btn-copy" title="Copy URL to clipboard">
              <img src="/images/copy-icon.svg" width="13" height="15" alt="" />
              <span id="labelCopied" className="label-copied">
                copied
              </span>
            </i>
          </p>
          <p className="text-center" style={{ fontSize: '.8rem' }}>
            Login here to check your stats:
            <br />
            <a href="/" id="hashAdmin">
              abc
            </a>
          </p>
        </article>
      )}

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
