--! Purpose: parse HTML code.
-- Based upon Roberto Ierusalimschy simple XML parser
-- Adopted to parse HTML by Leo Razoumov
-- Send bug reports to Leo Razoumov <slonik.az@gmail.com>

local error,assert,type= 
      error,assert,type
local      find,       gsub,       sub,      concat,      insert,      remove=
    string.find,string.gsub,string.sub,table.concat,table.insert,table.remove

-- wrap up module. 
module(...) --no old global space below this point
--------------------------------------------------------------------------------

local empty_elements= { --lists all HTML empty (void) elements
	br      = true,
	img     = true,
	meta    = true,
	META    = true,
	frame   = true,
	area    = true,
	hr      = true,
	base    = true,
	col     = true,
	link    = true,
	input   = true,
	option  = true,
	param   = true,
}

local function parseargs(s)
    local arg = {}
    gsub(s, "(%w+)=([\"'])(.-)%2", function (w, _, a) arg[w] = a end)
    return arg
end

--[[collect: parses HTML code and returns corresponding tree as a Lua table
    @s - HTML code as a string
--]]    
local function collect(s)
    local stack = {}
    local top = {}
    insert(stack, top)
    local ni,c,element,xarg, empty
    local i, j = 1, 1
    while true do
        ni,j,c,element,xarg, empty = find(s, "<(%/?)([%w:]+)(.-)(%/?)>", i)
        if not ni then break end
        if empty_elements[element] then empty= '/' end
        local text = sub(s, i, ni-1)
        if not find(text, "^%s*$") then
            insert(top, text)
        end
        if empty == "/" then    -- empty element tag
            insert(top, {element=element, xarg=parseargs(xarg), empty=1})
        elseif c == "" then     -- start tag
            top = {element=element, xarg=parseargs(xarg)}
            insert(stack, top)  -- new level
        else  -- end tag
            local toclose = remove(stack)  -- remove top
            top = stack[#stack]
            if #stack < 1 then
                error("nothing to close with "..element)
            end
            if toclose.element ~= element then
                error("trying to close "..toclose.element.." with "..element)
            end
            insert(top, toclose)
        end
        i = j+1
    end
    local text = sub(s, i)
    if not find(text, "^%s*$") then
        insert(stack[#stack], text)
    end
    if #stack > 1 then
        error("unclosed "..stack[#stack].element)
    end
    return stack[1]
end
_M.collect = collect --export module function

--------------------------------------------------------------------------------
--|> EMACS customization section.
-- LOCAL VARIABLES: 
-- mode:        Lua
-- coding:      utf-8
-- default-input-method: cyrillic-translit
-- fill-column: 88
-- tab-width:   4
-- END:
