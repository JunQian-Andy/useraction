#!/opt/pro/python279/bin/python2.7
# -*- coding: utf-8 -*-
import date_helper, re, time, json, mysql_helper, log_helper


logtime = date_helper.get_add_hourst3(-6)
#apilog_file = '/tmp/apilogi%s.log' %(logtime)
apilog_file = '/data/Tree/player/apilog/apilogi%s.log' %(logtime)
print apilog_file
global __log__path 
__log__path = "/data/log/useraction/action.log"

def logger(mes):
   log_helper.get_logger(__log__path).info(mes)


def select_line(matching, content):
    rc = re.findall(matching, content)
    return rc

def log_line(file):
    f = open(file, 'r')
    line = f.readline()
    while line:
        yield line.replace(r'action:','"action":').split("|")
        line = f.readline()
    f.close()
    yield None


if __name__ == '__main__':
    import sys
    reload(sys)
    matching = r'"actionValue":411'
    #print(matching)
    for content in log_line(apilog_file):
        if type(content) == list:
            if re.search(r'^.*"actionValue":411',''.join(content)) != None:
                #print(content[9:-3])
                #print(content[3], content[5])
                action_dict = json.loads('|'.join(content[9:-3]))
                for i in action_dict['action']:
                    if i['actionValue'] == 411:
                        i['mobile'] = content[3]
                        i['network'] = content[5]
                        i['userID'] = content[0]
                        i['userName'] = content[1]
                        i['clientVer'] = content[4]
                        i['ip'] = content[6]
                        i['playerVer'] = i['value'].split('|')[1]
                        i['playPos'] = i['value'].split('|')[0]
                        del i['value']

                        logger(i)
                        sql = "INSERT INTO " \
                              "player_wait_info " \
                              "(userId, userName, contentId, clientVer, playerVer, url, " \
                              "playPos, actionTime, mobile, network, ip, createTime) " \
                              "VALUES " \
                              "(%s, %s, %s, %s, " \
                              "%s, %s, %s, %s, " \
                              "%s, %s, %s, now() ); "
			try:
			    params = (str(i['userID']), str(i['userName']), str(i['contentId']), str(i['clientVer']),\
			    	      str(i['playerVer']), str(i['url']), str(i['playPos']), str(i['actionTime']), \
                                      str(i['mobile']), str(i['network']), str(i['ip']), )
			except Exception as e:
                            print e

			mysql_helper.insert_or_update_or_delete(sql, params)
