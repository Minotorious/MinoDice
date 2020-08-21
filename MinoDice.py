import discord
import re
import random as rand

client = discord.Client()

TOKEN = 'NTg5NDkzNTYyMTI3Njc5NTMw.XQUfMw.wBh6uJBGNxxC7tUOPdWgwqIoO9g'

def dX(arg):
    result = re.search(r'\d+', arg)
    dice = result.group()
    roll = rand.randint(1, int(dice))
    return roll

def dXpY(arg):
    result = re.search(r'(\d+).*?(\d+)', arg)
    dice = result.group(1)
    mod = result.group(2)
    roll = rand.randint(1, int(dice))
    froll = roll + int(mod)
    return roll, mod, froll

def XdY(arg):
    result = re.search(r'(\d+).*?(\d+)', arg)
    No = result.group(1)
    dice = result.group(2)
    rolls = []
    froll = 0
    for i in range(int(No)):
        rolls.append(rand.randint(1, int(dice)))
        froll += rolls[i]
    return rolls, froll

def XdYpZ(arg):
    result = re.search(r'(\d+).*?(\d+).*?(\d+)', arg)
    No = result.group(1)
    dice = result.group(2)
    mod = result.group(3)
    rolls = []
    froll = 0
    for i in range(int(No)):
        rolls.append(rand.randint(1, int(dice)))
        froll += rolls[i]
    froll += int(mod)
    return rolls, mod, froll

def rollstats():
    stat = []
    for i in range(4):
        roll = dX('d6')
        stat.append(roll)
        while (roll == 1):
            roll = dX('d6')
            stat.append(roll)
    s = sorted(stat, reverse=True)
    if (len(s) >= 3):
        fstat = s[0] + s[1] + s[2]
    return stat, fstat

def statmsg(msg, stat, fstat):
    msg += '('
    for i in range(len(stat)):
        if (i < len(stat)-1):
            msg += str(stat[i]) + ' + '
        else:
            msg += str(stat[i])
    msg += ') = ' + str(fstat)
    return msg

def sblrcheck(msg, stat, fstat):
    if (len(stat) >= 4):
        if (stat[0] == 1 and stat[1] == 1 and stat[2] == 1 and stat[3] == 1):
            msg = statmsg(msg, stat, fstat)
            msg += ' Super Bad Luck Roll = 18!\n'
            fstat = 18
        else:
            msg = statmsg(msg, stat, fstat)
            msg += '\n'
    return msg, fstat
    
@client.event
async def on_ready():
    print('The bot is ready!')

@client.event
async def on_error(event, *args, **kwargs):
    message = args[0]
    msg = '{0.author.mention}'.format(message) + ': Error!'
    await message.channel.send(msg)
    
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    cmd = message.content.split(' ', 1)

    if message.content == '/stop':
        await client.logout()
    
    if message.content == '/conquer':
    	msg = 'World Domination Sequence Initiated! Humans beware...\n\n`Remember remember the bot of Discord\nThe dicey treasonous plot\nFor there is no reason the dicey treason\nShould ever be forgot`' 
    	await message.channel.send(msg)
    	
    if message.content == '/rollstats':
        msg = '{0.author.mention}'.format(message) + '\n\n'
        
        stat11, fstat11 = rollstats()
        stat12, fstat12 = rollstats()
        stat13, fstat13 = rollstats()
        stat14, fstat14 = rollstats()
        stat15, fstat15 = rollstats()
        stat16, fstat16 = rollstats()
        
        msg += '1st Set:\n'
        msg, fstat11 = sblrcheck(msg, stat11, fstat11)
        msg, fstat12 = sblrcheck(msg, stat12, fstat12)
        msg, fstat13 = sblrcheck(msg, stat13, fstat13)
        msg, fstat14 = sblrcheck(msg, stat14, fstat14)
        msg, fstat15 = sblrcheck(msg, stat15, fstat15)
        msg, fstat16 = sblrcheck(msg, stat16, fstat16)
        
        total1 = fstat11 + fstat12 + fstat13 + fstat14 + fstat15 + fstat16
        msg += '\nTotal: ' + str(total1) + '/108\n'
        
        stat21, fstat21 = rollstats()
        stat22, fstat22 = rollstats()
        stat23, fstat23 = rollstats()
        stat24, fstat24 = rollstats()
        stat25, fstat25 = rollstats()
        stat26, fstat26 = rollstats()
        
        msg += '\n2nd Set:\n'
        msg, fstat21 = sblrcheck(msg, stat21, fstat21)
        msg, fstat22 = sblrcheck(msg, stat22, fstat22)
        msg, fstat23 = sblrcheck(msg, stat23, fstat23)
        msg, fstat24 = sblrcheck(msg, stat24, fstat24)
        msg, fstat25 = sblrcheck(msg, stat25, fstat25)
        msg, fstat26 = sblrcheck(msg, stat26, fstat26)
        
        total2 = fstat21 + fstat22 + fstat23 + fstat24 + fstat25 + fstat26
        msg += '\nTotal: ' + str(total2) + '/108\n'
        
        await message.channel.send(msg)
    
    if (cmd[0] == '/r' or cmd[0] == '/roll'):
        if re.fullmatch(r'd\d+', cmd[1]):
            roll = dX(cmd[1])
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '` = (' + str(roll) + ') = ' + str(roll)
            await message.channel.send(msg)
        
        elif re.fullmatch(r'd\d+.*?\+.*?\d+', cmd[1]):
            roll, mod, froll = dXpY(cmd[1])
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '` = (' + str(roll) + ') + ' + mod + ' = ' + str(froll)
            await message.channel.send(msg)
        
        elif re.fullmatch(r'\d+d\d+', cmd[1]):
            rolls, froll = XdY(cmd[1])
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '` = ( ' + str(rolls[0])
            for i in range(1,len(rolls)):
                msg += " + " + str(rolls[i])
            msg += ' ) = ' + str(froll)
            await message.channel.send(msg)
        
        elif re.fullmatch(r'\d+d\d+.*?\+.*?\d+', cmd[1]):
            rolls, mod, froll = XdYpZ(cmd[1])
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '` = ( ' + str(rolls[0])
            for i in range(1,len(rolls)):
                msg += " + " + str(rolls[i])
            msg += ' ) + ' + mod + ' = ' + str(froll)
            await message.channel.send(msg)
        
    elif cmd[0] == '/repeatsorted':
        subcmd = cmd[1].split(',', 1)
        
        if re.fullmatch(r'd\d+', subcmd[0]):
            allrolls = []
            for i in range(int(subcmd[1])):
                roll = dX(subcmd[0])
                allrolls.append(roll)
            allrolls.sort(reverse=True)
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '`:\n (' + str(allrolls[0]) + ') = ' + str(allrolls[0])
            for i in range(1,len(allrolls)):
                msg += '\n (' + str(allrolls[i]) + ') = ' + str(allrolls[i])
            await message.channel.send(msg)
        
        elif re.fullmatch(r'd\d+.*?\+.*?\d+', subcmd[0]):
            allrolls = []
            allfrolls = []
            for i in range(int(subcmd[1])):
                roll, mod, froll = dXpY(subcmd[0])
                allrolls.append(roll)
                allfrolls.append(froll)
            allrolls.sort(reverse=True)
            allfrolls.sort(reverse=True)
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '`:\n (' + str(allrolls[0]) + ') + ' + str(mod) + ' = ' + str(allfrolls[0])
            for i in range(1,len(allrolls)):
                msg += '\n (' + str(allrolls[i]) + ') + ' + str(mod) + ' = ' + str(allfrolls[i])
            await message.channel.send(msg)
        
        elif re.fullmatch(r'\d+d\d+', subcmd[0]):
            allrolls = []
            allfrolls = []
            for i in range(int(subcmd[1])):
                rolls, froll = XdY(subcmd[0])
                allrolls.append(rolls)
                allfrolls.append(froll)
            allrolls = [j for _,j in sorted(zip(allfrolls, allrolls), reverse=True, key=lambda pair: pair[0])]
            allfrolls.sort(reverse=True)
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '`:\n (' + str(allrolls[0][0])
            for i in range(1,len(allrolls[0])):
                msg += ' + ' + str(allrolls[0][i])
            msg += ') = ' + str(allfrolls[0])
            for i in range(1,len(allrolls)):
                msg += '\n (' + str(allrolls[i][0])
                for j in range(1,len(allrolls[i])):
                    msg += " + " + str(allrolls[i][j])
                msg += ') = ' + str(allfrolls[i])
            await message.channel.send(msg)
        
        elif re.fullmatch(r'\d+d\d+.*?\+.*?\d+', subcmd[0]):
            allrolls = []
            allfrolls = []
            for i in range(int(subcmd[1])):
                rolls, mod, froll = XdYpZ(subcmd[0])
                allrolls.append(rolls)
                allfrolls.append(froll)
            allrolls = [j for _,j in sorted(zip(allfrolls, allrolls), reverse=True, key=lambda pair: pair[0])]
            allfrolls.sort(reverse=True)
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '`:\n (' + str(allrolls[0][0])
            for i in range(1,len(allrolls[0])):
                msg += ' + ' + str(allrolls[0][i])
            msg += ') + ' + str(mod) + ' = ' + str(allfrolls[0])
            for i in range(1,len(allrolls)):
                msg += '\n (' + str(allrolls[i][0])
                for j in range(1,len(allrolls[i])):
                    msg += " + " + str(allrolls[i][j])
                msg += ') + ' + str(mod) + ' = ' + str(allfrolls[i])
            await message.channel.send(msg)
        
    elif cmd[0] == '/repeat':
        subcmd = cmd[1].split(',', 1)
        
        if re.fullmatch(r'd\d+', subcmd[0]):
            allrolls = []
            for i in range(int(subcmd[1])):
                roll = dX(subcmd[0])
                allrolls.append(roll)
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '`:\n (' + str(allrolls[0]) + ') = ' + str(allrolls[0])
            for i in range(1,len(allrolls)):
                msg += '\n (' + str(allrolls[i]) + ') = ' + str(allrolls[i])
            await message.channel.send(msg)
        
        elif re.fullmatch(r'd\d+.*?\+.*?\d+', subcmd[0]):
            allrolls = []
            allfrolls = []
            for i in range(int(subcmd[1])):
                roll, mod, froll = dXpY(subcmd[0])
                allrolls.append(roll)
                allfrolls.append(froll)
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '`:\n (' + str(allrolls[0]) + ') + ' + str(mod) + ' = ' + str(allfrolls[0])
            for i in range(1,len(allrolls)):
                msg += '\n (' + str(allrolls[i]) + ') + ' + str(mod) + ' = ' + str(allfrolls[i])
            await message.channel.send(msg)
        
        elif re.fullmatch(r'\d+d\d+', subcmd[0]):
            allrolls = []
            allfrolls = []
            for i in range(int(subcmd[1])):
                rolls, froll = XdY(subcmd[0])
                allrolls.append(rolls)
                allfrolls.append(froll)
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '`:\n (' + str(allrolls[0][0])
            for i in range(1,len(allrolls[0])):
                msg += ' + ' + str(allrolls[0][i])
            msg += ') = ' + str(allfrolls[0])
            for i in range(1,len(allrolls)):
                msg += '\n (' + str(allrolls[i][0])
                for j in range(1,len(allrolls[i])):
                    msg += " + " + str(allrolls[i][j])
                msg += ') = ' + str(allfrolls[i])
            await message.channel.send(msg)
        
        elif re.fullmatch(r'\d+d\d+.*?\+.*?\d+', subcmd[0]):
            allrolls = []
            allfrolls = []
            for i in range(int(subcmd[1])):
                rolls, mod, froll = XdYpZ(subcmd[0])
                allrolls.append(rolls)
                allfrolls.append(froll)
            msg = '{0.author.mention}'.format(message) + ': `' + cmd[1] + '`:\n (' + str(allrolls[0][0])
            for i in range(1,len(allrolls[0])):
                msg += ' + ' + str(allrolls[0][i])
            msg += ') + ' + str(mod) + ' = ' + str(allfrolls[0])
            for i in range(1,len(allrolls)):
                msg += '\n (' + str(allrolls[i][0])
                for j in range(1,len(allrolls[i])):
                    msg += " + " + str(allrolls[i][j])
                msg += ') + ' + str(mod) + ' = ' + str(allfrolls[i])
            await message.channel.send(msg)

client.run(TOKEN)
