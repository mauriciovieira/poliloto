function megasena(args)
    local title = 'Resultados da Mega-sena'
    if args.title then
        return title 
    elseif args[2] == 1 then
        return "11/03/1996"
    else 
        return '15.591.365,07'
    end
end
