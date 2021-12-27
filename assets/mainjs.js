console.log('hell world')

const counter = document.getElementById('counter')
let counterVal = parseInt(counter.textContent) //or set it to 0

let customerSize = 0
const updateTime = 100
const tresh = 300
let counted = false

const runCounter = () => {
    window.addEventListener('scroll', e => {
        let position = window.scrollY
        if (position > tresh && !counted) {
            counted = true
            const runCount = setInterval(() => {
                console.log('hello world')
                if (counterVal < customerSize) {
                    counterVal++
                    counter.textContent = counterVal
                } else {
                    clearInterval(runCount)
                }
            }, updateTime)
        }
    })
}


$.ajax({
    type: 'GET',
    url: '/customers-json/',
    success: function(response) {
        customerSize = response.customer_count
        runCounter()
    },
    error: function(error) {
        console.log(error)
    }
})