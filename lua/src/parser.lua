local html = require 'lib.html'

function megasena(args)

    io.input('../resultados/D_MEGA.HTM')
    local h = io.read("*all")
    local parsed = html.collect(h)

    local title = 'Resultados da Mega-sena'
    if args.title then
        return title 
    elseif args[2] == 1 then
        return "11/03/1996"
    else 
        return '15.591.365,07'
    end
end
