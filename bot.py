import datetime, pytz
from tokenize import Number
from logging import _srcfile
import csv
import copy
from time import sleep
import discord
import asyncio
from ro_py import Client
import random
import os
Rclient = Client()
client = discord.Client()

#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
desc_pattern = ["Hello", "Hi", "School", "Nice", "Good", "Great", "Study", "Kim", "Core", "You"]
"""
 - Memo - 
플레이어 데이터 저장순서
ID 닉네임(Rbx) > 닉네임(Dsc) > 넘버

w : (write 모드) 새로 파일을 쓸 때 사용
r : (read 모드) 파일로부터 데이터를 읽고 싶을 때 사용
a : (append 모드) 파일에 데이터를 추가로 쓰고 싶을 때 사용
"""

Verify_Step_1 = []
Verify_Step_2 = []
Verify_Step_3 = []
Connect_Group_Step_1 = []
Connect_Group_Step_2 = []
needer = False
plr = False
Pattern_ = False
amount = False

@client.event
async def on_ready():
    print("SCP DT - BOT READY", datetime.datetime.now(pytz.timezone('UTC')))
    Rclient.token_login("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_64A70198B64CDC0CF9C7EF89DAAC378ECBA65F1A763DD8C9FD07A74331AD02D4FFA0FDDB4414C81819314BA13501B571572E749D62755AB6DA747F7798E3BA8903AC67A598412018A10F3C81DFFAF2BF619AF3D9BF2638CBA226644941E731940513FFAF8F6CA5B2CA37A8B7386D50AAFE06A605F0CDD3312445851F3CF53B147ACFC8AC7CD9F375C2B097A434077B914B78A2895E262A9FEE3132C4264ED86D1A20145650B16F2DA78FCE501B35FA0DA29D7134AE3091D49CBAB255CA55637165C2F881C7962554A2F463FAE015B69229407AB763173DA3C300D7119CDB7A4C4402E69DF683615E436B3DBF7D52C54C62617875E0ACD79B2E83CE526E0969917F0AB517E6887A9572CE709432E2293488CEBFB467B3BB92E2047C86CB039E34BCBC789747FE9C61A35A823271BA0023CF27003B88B797992194AD3F54754D3F02B6B6D6")
    await client.change_presence(status=discord.Status.online , activity=discord.Game("SYSTEM ON - RESPONSE READY"))
    #2876297065
    #_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_64A70198B64CDC0CF9C7EF89DAAC378ECBA65F1A763DD8C9FD07A74331AD02D4FFA0FDDB4414C81819314BA13501B571572E749D62755AB6DA747F7798E3BA8903AC67A598412018A10F3C81DFFAF2BF619AF3D9BF2638CBA226644941E731940513FFAF8F6CA5B2CA37A8B7386D50AAFE06A605F0CDD3312445851F3CF53B147ACFC8AC7CD9F375C2B097A434077B914B78A2895E262A9FEE3132C4264ED86D1A20145650B16F2DA78FCE501B35FA0DA29D7134AE3091D49CBAB255CA55637165C2F881C7962554A2F463FAE015B69229407AB763173DA3C300D7119CDB7A4C4402E69DF683615E436B3DBF7D52C54C62617875E0ACD79B2E83CE526E0969917F0AB517E6887A9572CE709432E2293488CEBFB467B3BB92E2047C86CB039E34BCBC789747FE9C61A35A823271BA0023CF27003B88B797992194AD3F54754D3F02B6B6D6

@client.event
async def on_message(message):
    with open('TierServer.csv', 'r', encoding='UTF8') as f:
        rdr = csv.reader(f)
        for line in rdr:
            if str(message.guild.id) in line:
                global needer
                global Verify_Step_1
                global Verify_Step_2
                global Verify_Step_3
                global plr
                global Pattern_
                global amount
                if message.content.startswith("DEBUG - Verifyng Personnel"):
                    embed = discord.Embed(title="현재 인증중인 인원", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                    embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                    embed.add_field(name="Step - 1", value = Verify_Step_1, inline=False)
                    embed.add_field(name="Step - 2", value = Verify_Step_2, inline=False)
                    embed.add_field(name="Step - 3", value = Verify_Step_3, inline=False)
                    await message.channel.send(embed=embed)
                elif message.author.id not in Verify_Step_1 and message.author.id not in Verify_Step_2 and message.author.id not in Verify_Step_3:
                    with open('TierServer.csv', 'r', encoding='UTF8') as f:
                        if message.content.startswith(";문서"):
                            amount = message.content[4:]
                            embed = discord.Embed(title="데이터 베이스가 정상적으로 추출 및 전송되었습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)

                            embed.add_field(name="문서", value="http://ko.scp-wiki.net/{}".format(amount), inline=False)
                            embed.add_field(name="요청자", value=message.author.mention, inline=False)

                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                            await message.channel.send (embed=embed)
                            if message.content == (";추천문서"):
                                embed = discord.Embed(title="추천문서", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                embed.add_field(name="SCP:KR 메인", value="http://ko.scp-wiki.net/", inline=True)
                                embed.add_field(name="SCP재단에 대하여", value="http://ko.scp-wiki.net/about-the-scp-foundation", inline=True)
                                embed.add_field(name="-", value="SCP 개체", inline=False)
                                embed.add_field(name="SCP - I", value="http://ko.scp-wiki.net/scp-series", inline=True)
                                embed.add_field(name="SCP - II", value="http://ko.scp-wiki.net/scp-series-2", inline=True)
                                embed.add_field(name="SCP - III", value="http://ko.scp-wiki.net/scp-series-3", inline=True)
                                embed.add_field(name="SCP - IV", value="http://ko.scp-wiki.net/scp-series-4", inline=True)
                                embed.add_field(name="SCP - V", value="http://ko.scp-wiki.net/scp-series-5", inline=True)
                                embed.add_field(name="SCP - VI", value="http://ko.scp-wiki.net/scp-series-6", inline=True)
                                embed.add_field(name="SCP - VII", value="http://ko.scp-wiki.net/scp-series-7", inline=True)
                                embed.add_field(name="SCP - KO", value="http://ko.scp-wiki.net/scp-series-ko", inline=True)
                                embed.add_field(name="-", value="기동특무부대", inline=False)
                                embed.add_field(name="기동특무부대", value="http://ko.scp-wiki.net/task-forces", inline=True)
                                embed.add_field(name="기동특무부대 - KR", value="http://ko.scp-wiki.net/task-forces", inline=True)
                                embed.add_field(name="-", value="등급", inline=False)
                                embed.add_field(name="보안인가등급", value="http://ko.scp-wiki.net/security-clearance-levels", inline=True)
                                embed.add_field(name="객체등급", value="http://ko.scp-wiki.net/object-classes", inline=True)
                                embed.add_field(name="-", value="Area Alpha 문서", inline=False)
                                embed.add_field(name="부서/직급 설명(비공식)", value="https://docs.google.com/document/d/1Y75NrG8ZHeYM76EsKn_6O1mfji-O6_3NfXbf6uFFNc4/edit?usp=sharing", inline=True)
                                embed.add_field(name="프로토콜(비공식)", value="https://docs.google.com/document/d/1Q_jWPGzI5bFy5P5SN4qDX75doaHj66fl3Hhu266ogMM/edit?usp=sharing", inline=True)
                                embed.add_field(name="부서/직급별 규칙(비공식)", value="https://docs.google.com/document/d/1_VGpBz8SN5vf-UQjX7R8a_UEfKEpv_P8Hf1NYs7ziQs/edit?usp=sharing", inline=True)

                                embed.add_field(name="요청자", value=message.author.mention, inline=False)
                                embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                await message.channel.send (embed=embed)
                        if message.content.startswith (";영어문서"):
                            amount = message.content[6:]
                            embed = discord.Embed(title="데이터 베이스가 정상적으로 추출 및 전송되었습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)

                            embed.add_field(name="문서", value="http://scp-wiki.wikidot.com/{}".format(amount), inline=False)
                            embed.add_field(name="요청자", value=message.author.mention, inline=False)

                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                            await message.channel.send (embed=embed)
                        if message.content == (";추천문서"):
                            embed = discord.Embed(title="추천문서", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                            embed.add_field(name="SCP:KR 메인", value="http://ko.scp-wiki.net/", inline=True)
                            embed.add_field(name="SCP재단에 대하여", value="http://ko.scp-wiki.net/about-the-scp-foundation", inline=True)
                            embed.add_field(name="-", value="SCP 개체", inline=False)
                            embed.add_field(name="SCP - I", value="http://ko.scp-wiki.net/scp-series", inline=True)
                            embed.add_field(name="SCP - II", value="http://ko.scp-wiki.net/scp-series-2", inline=True)
                            embed.add_field(name="SCP - III", value="http://ko.scp-wiki.net/scp-series-3", inline=True)
                            embed.add_field(name="SCP - IV", value="http://ko.scp-wiki.net/scp-series-4", inline=True)
                            embed.add_field(name="SCP - V", value="http://ko.scp-wiki.net/scp-series-5", inline=True)
                            embed.add_field(name="SCP - VI", value="http://ko.scp-wiki.net/scp-series-6", inline=True)
                            embed.add_field(name="SCP - VII", value="http://ko.scp-wiki.net/scp-series-7", inline=True)
                            embed.add_field(name="SCP - KO", value="http://ko.scp-wiki.net/scp-series-ko", inline=True)
                            embed.add_field(name="-", value="기동특무부대", inline=False)
                            embed.add_field(name="기동특무부대", value="http://ko.scp-wiki.net/task-forces", inline=True)
                            embed.add_field(name="기동특무부대 - KR", value="http://ko.scp-wiki.net/task-forces", inline=True)
                            embed.add_field(name="-", value="등급", inline=False)
                            embed.add_field(name="보안인가등급", value="http://ko.scp-wiki.net/security-clearance-levels", inline=True)
                            embed.add_field(name="객체등급", value="http://ko.scp-wiki.net/object-classes", inline=True)
                            embed.add_field(name="-", value="Area Alpha 문서", inline=False)
                            embed.add_field(name="부서/직급 설명(비공식)", value="https://docs.google.com/document/d/1Y75NrG8ZHeYM76EsKn_6O1mfji-O6_3NfXbf6uFFNc4/edit?usp=sharing", inline=True)
                            embed.add_field(name="프로토콜(비공식)", value="https://docs.google.com/document/d/1Q_jWPGzI5bFy5P5SN4qDX75doaHj66fl3Hhu266ogMM/edit?usp=sharing", inline=True)
                            embed.add_field(name="부서/직급별 규칙(비공식)", value="https://docs.google.com/document/d/1_VGpBz8SN5vf-UQjX7R8a_UEfKEpv_P8Hf1NYs7ziQs/edit?usp=sharing", inline=True)

                            embed.add_field(name="요청자", value=message.author.mention, inline=False)
                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                            await message.channel.send (embed=embed)
                    if message.content.startswith(";인증"):
                        needer = str(message.author.id)
                        try:
                            f = open("Data.csv", "r", encoding = "UTF-8")
                            rdr = csv.reader(f)
                            Strings = ""
                            for r in rdr:
                                print(str(message.author.id) in r)
                                if str(message.author.id) in r:
                                    Strings = r
                                    print("Found", Strings)
                                    break
                                if str(message.author.id) not in r:
                                    Strings = False
                                    print("404", Strings)
                            f.close()
                            if not Strings is False:
                                print("Result <{}>".format(Strings))
                                print("ID <{}>".format(Strings[0]))
                                print("Rbx Name <{}>".format(Strings[1]))
                                print("Dsc Name <{}>".format(Strings[2]))
                                print("Dsc Tag <{}>".format(Strings[3]))
                                
                                embed = discord.Embed(title="플레이어 {}와 연동되어있습니다. 재인증 하시겠습니까?".format(Strings[1]), description="다른 계정과 연동 \'예\', 현재 계정으로 인증하려면 \'아니오\', 취소하려면 \'취소\'",  timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                await message.channel.send (embed=embed)
                                print("Verify_1")
                                Verify_Step_1.append(message.author.id)
                                #del(needer)
                            if Strings is False:
                                embed = discord.Embed(title="인증 하시겠습니까?", description="계정을 연동 \'예\', 취소하려면 \'취소\'",  timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                                embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                await message.channel.send (embed=embed)
                                Verify_Step_1.append(message.author.id)
                        except:
                            embed = discord.Embed(title="오류!", description="요청하신 유저를 찾지 못하였거나 오류가 발생하였습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                            await message.channel.send (embed=embed)
                    if message.content == "DEBUG":
                        print("BOT READY")
                        await message.author.send ("{} BOT READY".format(message.author.mention))
                    if message.content.startswith (";청소"):
                        i = (message.author.guild_permissions.administrator)

                        if i is True:
                            amount = message.content[4:]
                            await message.channel.purge(limit=1)
                            await message.channel.purge(limit=int(amount))
                        if i is False:
                            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))
                    if message.content == (";도움말"):
                        embed = discord.Embed(title="도움말", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                        embed.add_field(name=";도움말", value="도움말을 출력합니다. (ex. ;도움말", inline=False)
                        #embed.add_field(name=";문서", value="요청한 문서를 출력합니다. (ex. ;문서 <원하는 문서 url>", inline=False)
                        #embed.add_field(name=";영어문서", value="요청한 영어문서를 출력합니다. (ex. ;영어문서 <원하는 문서 url>", inline=False)
                        #embed.add_field(name=";추천문서", value="추천하는 문서를 출력합니다. (ex. ;추천문서", inline=False)
                        embed.add_field(name=";정보", value="원하는 유저의 정보를 출력합니다. (ex. ;정보 <닉네임(디스플레이 닉네임 X)>", inline=False)
                        embed.add_field(name=";진급", value="원하는 유저를 진급합니다. (ex. ;진급 <닉네임(디스플레이 닉네임 X)>", inline=False)
                        embed.add_field(name=";강등", value="원하는 유저를 강등합니다. (ex. ;강등 <닉네임(디스플레이 닉네임 X)>", inline=False)
                        embed.add_field(name=";역할정보", value="그룹에 있는 모든역할을 표시합니다. (ex. ;역할정보", inline=False)
                        embed.add_field(name=";그룹샤우트", value="그룹샤우트를 등록합니다. (ex. ;그룹샤우트 <원하는 텍스트>", inline=False)
                        embed.add_field(name=";그룹추방", value="원하는 유저를 추방합니다. (ex. ;그룹추방 <닉네임(디스플레이 닉네임 X)>", inline=False)
                        embed.add_field(name=";인증", value="인증합니다. (ex. ;인증", inline=False)
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send (embed=embed)
                    if message.content == ("Emergency Protocol - The Developer Face"):
                        await message.channel.send ("https://cdn.discordapp.com/attachments/753492252268953712/901398621751242762/20211023_180237.jpg")
                    if message.content == ("김인간 개잘생김"):
                        for i in range(1, 1000):
                            await message.author.send ("{} ㅇㅈ".format(message.author.mention))
                            await message.author.send ("{} 오우 뭘좀 아는 놈 이구만?".format(message.author.mention))
                    if message.content.startswith(";정보"):
                        amount = message.content[4:]
                        group_id_ = line[1]
                        print(amount)
                        try:
                            plr = await Rclient.get_user_by_username(amount)
                            SCP_Group = await Rclient.get_group(group_id_)
                            
                            try:
                                Group_plr = await SCP_Group.get_member_by_id(plr.id)
                                plr_Rank = Group_plr.role
                            except:
                                plr_Rank = "None."
                            
                            embed = discord.Embed(title=plr.name, url="https://web.roblox.com/users/{}/profile".format(plr.id), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                            embed.add_field(name="디스플레이 닉네임", value=plr.display_name or 'None', inline=False)
                            embed.add_field(name="계정 관련", value=" - - ", inline=False)
                            embed.add_field(name="상태 메세지", value=await plr.get_status() or 'None', inline=True)
                            embed.add_field(name="계정 생성일", value=plr.created.strftime("%m/%d/%Y, %H:%M:%S" or 'None'), inline=True)
                            embed.add_field(name="계정 설명", value=plr.description or 'None', inline=False)
                            embed.add_field(name="그룹 관련", value=" - - ", inline=False)
                            embed.add_field(name="그룹 역할", value= plr_Rank or 'None', inline=True)
                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                            await message.channel.send (embed=embed)
                        except:
                            embed = discord.Embed(title="오류!", description="요청하신 유저를 찾지 못하였거나 오류가 발생하였습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                            await message.channel.send (embed=embed)
                    if message.content.startswith(";강등"):
                        i = (message.author.guild_permissions.administrator)
                        with open('TierServer.csv', 'r', encoding='UTF8') as f:
                            rdr = csv.reader(f)
                            for line in rdr:
                                if str(message.guild.id) in line:
                                    group_id_ = line[1]
                                    try:
                                        if i is True:
                                            amount = message.content[4:]
                                            print(amount)
                                            SCP_Group = await Rclient.get_group(group_id_)
                                            plr = await Rclient.get_user_by_username(amount)
                                            Group_plr = await SCP_Group.get_member_by_id(plr.id)
                                            await Group_plr.demote()
                                            embed = discord.Embed(title="{}, 강등됨".format(plr.name), url="https://web.roblox.com/users/{}/profile".format(plr.id), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                                            #embed.add_field(name="현재 계급", value=plr_Rank_.name, inline=False)
                                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                            await message.channel.send (embed=embed)
                                        if i is False:
                                            embed = discord.Embed(title="오류!", description="요청자에게 권한이 없습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                            await message.channel.send (embed=embed)
                                    except:
                                        embed = discord.Embed(title="오류!", description="요청하신 유저를 찾지 못하였거나 오류가 발생하였습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                        await message.channel.send (embed=embed)
                    if message.content.startswith(";진급"):
                        i = (message.author.guild_permissions.administrator)
                        with open('TierServer.csv', 'r', encoding='UTF8') as f:
                            rdr = csv.reader(f)
                            for line in rdr:
                                if str(message.guild.id) in line:
                                    group_id_ = line[1]
                                    try:
                                        if i is True:
                                            amount = message.content[4:]
                                            print(amount)
                                            SCP_Group = await Rclient.get_group(group_id_)
                                            plr = await Rclient.get_user_by_username(amount)
                                            Group_plr = await SCP_Group.get_member_by_id(plr.id)
                                            await Group_plr.demote()
                                            embed = discord.Embed(title="{}, 진급됨".format(plr.name), url="https://web.roblox.com/users/{}/profile".format(plr.id), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                                            #embed.add_field(name="현재 계급", value=plr_Rank_.name, inline=False)
                                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                            await message.channel.send (embed=embed)
                                        if i is False:
                                            embed = discord.Embed(title="오류!", description="요청자에게 권한이 없습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                            await message.channel.send (embed=embed)
                                    except:
                                        embed = discord.Embed(title="오류!", description="요청하신 유저를 찾지 못하였거나 오류가 발생하였습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                        await message.channel.send (embed=embed)
                    if message.content.startswith(";역할정보"):
                        with open('TierServer.csv', 'r', encoding='UTF8') as f:
                            rdr = csv.reader(f)
                            for line in rdr:
                                if str(message.guild.id) in line:
                                    group_id_ = line[1]
                                    try:
                                        amount = message.content[6:]
                                        print(amount)
                                        SCP_Group = await Rclient.get_group(group_id_)
                                        Texty = ""
                                        
                                        
                                        SCP_Group_Roles = await SCP_Group.get_roles()
                                        for i in SCP_Group_Roles:
                                            if not i.name == "Guest":
                                                Texty += "[ 이름 - {} / 계급 - {} ]\n".format(i.name, i.rank)

                                        embed = discord.Embed(title="역할정보", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                                        embed.add_field(name="현재 계급", value= Texty, inline=False)
                                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                        await message.channel.send (embed=embed)
                                    except:
                                        embed = discord.Embed(title="오류!", description="요청하신 유저를 찾지 못하였거나 오류가 발생하였습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                        await message.channel.send (embed=embed)
                    if message.content.startswith(";그룹추방"):
                        amount = message.content[6:]
                        i = (message.author.guild_permissions.administrator)
                        with open('TierServer.csv', 'r', encoding='UTF8') as f:
                            rdr = csv.reader(f)
                            for line in rdr:
                                if str(message.guild.id) in line:
                                    group_id_ = line[1]
                                    try:
                                        if i is True:
                                            SCP_Group = await Rclient.get_group(group_id_)
                                            plr = await Rclient.get_user_by_username(amount)
                                            Group_plr = await SCP_Group.get_member_by_id(plr.id)
                                            await Group_plr.exile()
                                            embed = discord.Embed(title="플레이어 {}가 성공적으로 추방됬습니다.".format(plr.name), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                            await message.channel.send (embed=embed)
                                        if i is False:
                                            embed = discord.Embed(title="오류!", description="요청자에게 권한이 없습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                            await message.channel.send (embed=embed)
                                    except:
                                        embed = discord.Embed(title="오류!", description="요청하신 유저를 찾지 못하였거나 오류가 발생하였습니다. 다시 시도해 주세요.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                        await message.channel.send (embed=embed)
                    if message.content.startswith(";그룹샤우트"):
                        amount = message.content[7:]
                        i = (message.author.guild_permissions.administrator)
                        with open('TierServer.csv', 'r', encoding='UTF8') as f:
                            rdr = csv.reader(f)
                            for line in rdr:
                                if str(message.guild.id) in line:
                                    try:
                                        if i is True:
                                            group_id_ = line[1]
                                            SCP_Group = await Rclient.get_group(group_id_)
                                            await SCP_Group.update_shout(amount)
                                            """if "#" in shout:
                                                await SCP_Group.update_shout(old_shout)
                                                embed = discord.Embed(title="오류!", description="요청하신 메세지가 필터링됬습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                                embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                                await message.channel.send (embed=embed)
                                            else:"""
                                            embed = discord.Embed(title="요청하신 메세지가 성공적으로 입력됬습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                            await message.channel.send (embed=embed)
                                        if i is False:
                                            embed = discord.Embed(title="오류!", description="요청자에게 권한이 없습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                            await message.channel.send (embed=embed)
                                    except:
                                        embed = discord.Embed(title="오류!", description="오류가 발생하였습니다. 다시 시도해 주세요.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                        await message.channel.send (embed=embed)
                    if message.content.startswith(";업데이트"):
                        f = open('Data.csv', 'r', encoding='UTF8')
                        rdr = csv.reader(f)
                        for r in rdr:
                            if str(message.author.id) in r:
                                Strings = copy.deepcopy(r)
                                Founded = True
                                print("Found", Strings)
                                break
                            if str(message.author.id) not in r:
                                Strings = False
                                Founded = False
                                #print("404", Strings)
                        if Founded is True:
                            plr = await Rclient.get_user_by_username(Strings[1])
                            plus_mention = ""
                            minus_mention = ""
                            Roles_list = []
                            with open('TierServer.csv', 'r', encoding='UTF8') as f:
                                rdr = csv.reader(f)
                                for line in rdr:
                                    if str(message.guild.id) in line:
                                        del line[:3]
                                        for element in line:
                                            elements = element.split("$")
                                            group_id = elements[0]
                                            role_id = elements[1]
                                            print(group_id)
                                            print(role_id)
                                            group = await Rclient.get_group(int(group_id))
                                            #try:
                                            print(Strings[1])
                                            try:
                                                Found = True
                                                group_plr = await group.get_member_by_username(Strings[1])
                                            except:
                                                Found = False
                                            if Found:
                                                plus_mention = "{}{}".format(plus_mention, "{}\n".format("<@&{}>".format(role_id)))
                                                guild = message.guild
                                                role = discord.utils.get(guild.roles, id=int(role_id))
                                                await message.author.add_roles(role)
                                            else:
                                                minus_mention = "{}{}".format(minus_mention, "{}\n".format("<@&{}>".format(role_id)))
                                                guild = message.guild
                                                role = discord.utils.get(guild.roles, id=int(role_id))
                                                await message.author.remove_roles(role)
                                            #except:
                                                #pass
                            print(plus_mention, "\n", minus_mention)
                            embed = discord.Embed(title="업데이트 되었습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                            if plus_mention != "":
                                embed.add_field(name="+ 추가된 역할 +", value = plus_mention, inline=False)
                            else:
                                embed.add_field(name="+ 추가된 역할 +", value = "없음", inline=False)
                            if minus_mention != "":
                                embed.add_field(name="- 삭제된 역할 -", value = minus_mention, inline=False)
                            else:
                                embed.add_field(name="- 삭제된 역할 -", value = "없음", inline=False)
                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                            await message.channel.send(embed=embed)
                        elif Founded is False:
                            embed = discord.Embed(title="요청자가 인증되어 있지 않습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                            await message.channel.send(embed=embed)
                        f.close()
                    if message.content.startswith(";서브그룹연동"):
                        needer = str(message.author.id)
                        try:
                            i = (message.author.guild_permissions.administrator)
                            if i is True:
                                embed = discord.Embed(title="인증 하시겠습니까?", description="그룹의 ID를 입력해주세요. 취소하려면 \'취소\'",  timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                                embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                                await message.channel.send (embed=embed)
                                Connect_Group_Step_1.append(needer)
                            if i is False:
                                await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))
                        except:
                            embed = discord.Embed(title="오류!", description="오류가 발생하였습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                            embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                            await message.channel.send (embed=embed)
                elif message.author.id in Verify_Step_1:
                    if message.content.startswith("예"):
                        embed = discord.Embed(title="닉네임을 말해주십시오.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send(embed=embed)
                        Verify_Step_2.append(message.author.id)
                        Verify_Step_1.remove(message.author.id)
                    elif message.content.startswith("아니오"):
                        embed = discord.Embed(title="취소됨", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send (embed=embed)
                        Verify_Step_1.remove(message.author.id)
                        return
                    elif message.content.startswith("취소"):
                        embed = discord.Embed(title="취소됨", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send (embed=embed)
                        Verify_Step_1.remove(message.author.id)
                        return
                    else:
                        embed = discord.Embed(title="취소됨", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send (embed=embed)
                        Verify_Step_1.remove(message.author.id)
                elif message.author.id in Verify_Step_2:
                    amount = message.content[0:]
                    try:
                        Found = True
                        plr = await Rclient.get_user_by_username(amount)
                    except:
                        Found = False
                    if Found is True:
                        Bfo = random.choice(desc_pattern),random.choice(desc_pattern),random.choice(desc_pattern),random.choice(desc_pattern)
                        Pattern_ = str(Bfo).replace(",","").replace("(","").replace(")","").replace("\'","")
                        del(Bfo)
                        embed = discord.Embed(title="유저가 확인됬습니다. {}({})".format(plr.name, plr.display_name), Description = "완료시 '완료', 취소하려면 \'취소\'" ,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                        embed.add_field(name="계정의 설명을 변경해주세요. (하셨다면 아무말이나 해주세요)", value=Pattern_, inline=False)
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/753492252268953712/920218574537240697/unknown.png")
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send (embed=embed) 
                        print(Pattern_, amount)
                        Verify_Step_3.append(message.author.id)
                        Verify_Step_2.remove(message.author.id)
                    if Found is False:
                        embed = discord.Embed(title="오류!", description="요청하신 유저를 찾지 못하였거나 오류가 발생하였습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send (embed=embed)
                        Verify_Step_2.remove(message.author.id)
                elif message.author.id in Verify_Step_3:
                    print(Pattern_)
                    plr = await Rclient.get_user_by_username(amount)
                    if plr.description == Pattern_:
                        embed = discord.Embed(title="성공!", description="계정 연동이 성공적으로 완료됬습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send (embed=embed)
                        print(plr.description, "Granted 1")
                        print("succes")
                        Verify_Step_1 = False
                        Verify_Step_2 = False
                        Verify_Step_3 = False
                        f = open('Data.csv', 'r', encoding='UTF8')
                        rdr = csv.reader(f)
                        for r in rdr:
                            print(str(message.author.id) in r)
                            if str(message.author.id) in r:
                                Strings = r
                                Founded = True
                                print("Found", Strings)
                                break
                            if str(message.author.id) not in r:
                                Strings = False
                                Founded = False
                                print("404", Strings)
                        if Founded is True:
                            f = open('Data.csv', 'r', encoding='UTF8')
                            lines = ""
                            Bfo = str(Strings[1])
                            Aft = plr.name
                            rdrss = csv.reader(f)
                            rdr = rdrss
                            for line in rdr:
                                linee = copy.deepcopy(line)
                                linee = str(linee).replace(Bfo, Aft)
                                print(linee)
                                lines = str(lines).replace("[","").replace("]","").replace("\'","").replace(" ","") + str(linee).replace("[","").replace("]","").replace("\'","").replace(" ","") + "\n"

                            f = open('Data.csv', 'w', encoding='UTF8', newline='')
                            f.write(str(lines).replace("(","").replace(")",""))
                            print(lines)
                            Verify_Step_3.remove(message.author.id)
                            needer = False
                            plr = False
                            Pattern_ = False
                            amount = False
                        if Founded is False:
                            f = open('Data.csv', 'a', encoding='UTF8', newline='')
                            f.write("\n{},{},{},{}".format(message.author.id, plr.name, message.author.name, message.author.discriminator))
                            Verify_Step_3.remove(message.author.id)
                            needer = False
                            plr = False
                            Pattern_ = False
                            amount = False
                        f.close()
                    elif plr.description != Pattern_:
                        embed = discord.Embed(title="실패!", description="계정의 설명이 같지 않습니다.", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x086d1c)
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send (embed=embed)
                        Verify_Step_3.remove(message.author.id)
                        needer = False
                        plr = False
                        Pattern_ = False
                        amount = False
                elif message.author.id in Connect_Group_Step_1:
                    try:
                        Found = True
                        Group = Rclient.get_group(int(message.content))
                    except:
                        Found = False
                    if Found:
                        pass
                    elif message.content.startswith("취소"):
                        embed = discord.Embed(title="취소됨", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send (embed=embed)
                        Verify_Step_1.remove(message.author.id)
                        return
                    else:
                        embed = discord.Embed(title="취소됨", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x992D22)
                        embed.set_footer(text="System By 김인간#1135 CC BY-SA", icon_url="https://cdn.discordapp.com/attachments/911794154147819570/926360317624217660/Core-TIer.png")
                        await message.channel.send (embed=embed)
                        Verify_Step_1.remove(message.author.id)

client.run(os.environ['ODgyODkyOTg1OTEyNjc2MzUy.YTCAKw.fcq1LHx25kgHAsMSX6zajvWZQNI'])
