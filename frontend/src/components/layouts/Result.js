import Clipboard from 'react-clipboard.js'
import { useHash } from '../../Contexts.js'

const Result = () => {
  const { hash } = useHash()
  const domain = process.env.REACT_APP_DOMAIN
  const hashLink = `${domain}/${hash}`
  const adminHashLink = `${domain}/${hash}+`

  return (
    <form className="form-shorten">
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

      <article className="panel result">
        <p className="text-center" style={{ paddingTop: '10px' }}>
          <img src="/images/done-icon.png" width="60" alt="" />
        </p>
        <p className="text-center">
          <b>
            Here is your new URL:
            <br />
            <a href={hashLink} id="hash">
              {hash}
            </a>
          </b>
          <Clipboard
            data-clipboard-text={hashLink}
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
        </p>
        <p className="text-center" style={{ fontSize: '.8rem' }}>
          Login here to check your stats:
          <br />
          <a href={adminHashLink} id="hashAdmin">
            {hash}+
          </a>
        </p>
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

export default Result
