local html = require 'lib.html'

function dict_zip(t1, t2)
    local res = {} 
    assert(table.getn(t1) == table.getn(t2))
    for i=1,table.getn(t1) do
        res[t1[i]] = t2[i]
    end
    return res
end

function get_elements(t)
    local res = {}
    for i=1,table.getn(t) do
            local value = ''
            if type(t[i][1]) == 'string' then
                value = t[i][1]
            elseif type(t[i][1][1]) == 'table' then
                value = t[i][1][1][1]
            end
            assert(type(value == 'string'))
            table.insert(res,value)
        end 
        return res
    end

function megasena()
    io.input('../resultados/D_MEGA.HTM')
    local h = io.read("*all")
    local raw = html.collect(h)
    local body = raw[1][2] -- body
    local main_table = body[3]

    local headers = get_elements(main_table[1]) --th s
    local concursos = {}
    for i=2,table.getn(main_table) do
        linha = get_elements(main_table[i])
        concurso = dict_zip(headers,linha)
        table.insert(concursos,concurso)
    end

    local parsed = {
        title = body[1][1][1][1][1][1],
        concursos = concursos,
    }
    return parsed
end
