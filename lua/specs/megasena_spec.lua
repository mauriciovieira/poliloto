require 'lib.luaspec'
require 'src.parser'

describe["Parser da megasena"] = function ()
    it ["A primeira frase deve ser Resultado da Mega-sena"] = function()
        expect (megasena()['title']).should_be("Resultado da Mega-sena")
    end

    it ["O primeiro concurso foi em 11/03/1996"] = function()
        expect (megasena()["concursos"][1]["Data Sorteio"]).should_be("11/03/1996")
    end
    
    it ["O premio do concurso 11 foi 15.591.365,07"] = function()
        local res = '15.591.365,07'
        expect(megasena()["concursos"][11]["Rateio_Sena"]).should_be(res)
    end
end

spec:report(false)
