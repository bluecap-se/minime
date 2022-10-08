process.stdin.on("data", data => {
    const {entrypoints, ...rest} = JSON.parse(data)
    console.log(JSON.stringify({
        "files": entrypoints,
        "version": process.env.VERSION
    }))
})
